import datetime
import json
import os

import pandas as pd
import psycopg2
import requests
from math import ceil
from bs4 import BeautifulSoup
from sqlalchemy import create_engine

from col_and_connodity_name import col_dict, name_and_key
from config import pg_config
from sql import create_LME_cotr_table_cmd


def connectDb():
    conn = psycopg2.connect(user=pg_config['user'],
                            password=pg_config['password'],
                            host=pg_config['host'],
                            port=pg_config['port'],
                            database=pg_config['dbname'])
    return conn


def get_file_name(metal_name):
    try:
        r = requests.get(
            'https://www.lme.com/en-GB/Market-Data/Reports-and-data/Commitments-of-traders/' + metal_name)
        soup = BeautifulSoup(r.text, 'html.parser')
        hash_str = soup.find('div', {'class': 'paginator'}).get('data-arm-options')
        hash_str = hash_str.split('/')[-1][:-1]
        metal_url = 'https://www.lme.com/api/Lists/DownloadLinks/' + hash_str
        r = requests.get(metal_url)
        js = json.loads(r.text)
        files = list()
        for page_idx in range(ceil(js['total_items'] / 10)):
            url = metal_url + '?currentPage=' + str(page_idx)
            r = requests.get(url)
            js = json.loads(r.text)
            for items in js['content_items']:
                files.append(items['Url'])
    except:
        r = requests.get(
            'https://www.lme.com/Market-Data/Reports-and-data/Commitments-of-traders/' + metal_name)
        soup = BeautifulSoup(r.text, 'html.parser')
        temp = soup.find('ul', {'class': 'download-list'})
        files = list()
        a_tags = temp.find_all('a')
        for tag in a_tags:
            a = tag.get('href')
            if a != '#':
                files.append(a)
    return files


def Download(name):
    url = "https://www.lme.com" + name
    resp = requests.get(url)

    if resp.status_code == 200:
        file_path = os.path.join(os.path.basename(url))
        with open(file_path, 'wb') as file:
            file.write(resp.content)
        return file_path


def process(filename, dict):
    df = pd.read_excel(filename)
    date = df['London Metal Exchange'][1]
    contract = df['London Metal Exchange'][4] if pd.notna(df['London Metal Exchange'][4]) else "NA"
    df = df[8:].drop(['London Metal Exchange', 'Unnamed: 1', 'Unnamed: 2'], axis=1).reset_index(drop=True)
    tmp = 0
    data = {'date': date, 'contract': contract}
    for j in range(11):
        for i in df.columns.values.tolist():
            if tmp >= 90 and tmp % 2:
                tmp += 1
                continue
            else:
                data[dict[str(tmp)]] = df[i][j]
                tmp += 1
    d = pd.DataFrame([data])
    return d


if __name__ == "__main__":
    conn = connectDb()
    cur = conn.cursor()
    cur.execute(create_LME_cotr_table_cmd)
    conn.commit()
    engine = create_engine('postgres://' + pg_config['user'] + ':' +
                           pg_config['password'] + '@' + pg_config['host'] + ':' +
                           str(pg_config['port']) + '/' + pg_config['dbname'])
    sql = "SELECT contract, max(date) as date from api_lme_cotr GROUP BY contract;"
    contract_df = pd.read_sql(sql, conn)

    for i in range(len(name_and_key)):
        name = list(name_and_key.keys())[i]
        # cur.execute(f"SELECT max(date) from api_lme_cotr where contract = '{name_and_key[name]}'")
        if contract_df.empty:
            latest = datetime.date(2018, 1, 1)
        else:
            latest = contract_df[contract_df.contract == name_and_key[name]]['date'].values[0]
        file_list = get_file_name(name)

        print(name_and_key[name], latest)
        for row in range(len(file_list)):
            check = file_list[0].split('-')[-3].split('/', 1)[-1]
            if datetime.datetime.strptime(check, "%Y/%M/%d").date() == latest:
                break
            file_date = file_list[-1 - row].split('-')[-3].split('/', 1)[-1]
            if datetime.datetime.strptime(file_date, "%Y/%M/%d").date() > latest:
                file_path = Download(file_list[-1 - row])
                df = process(file_path, col_dict)
                if df['contract'][0] == name_and_key[name]:
                    df.to_sql('api_lme_cotr', engine, index=False, if_exists='append')
                os.remove(file_path)
