import pandas as pd


def process(filename, dict):
    df = pd.read_excel(filename)
    date = df['London Metal Exchange'][1]
    contract = df['London Metal Exchange'][4]
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


col_dict = {
    '0': 'commercial_credit_long',
    '1': 'commercial_credit_short',
    '2': 'commercial_funds_long',
    '3': 'commercial_funds_short',
    '4': 'commercial_other_long',
    '5': 'commercial_other_short',
    '6': 'commercial_undertakings_long',
    '7': 'commercial_undertakings_short',
    '8': 'commercial_directive_long',
    '9': 'commercial_directive_short',
    '10': 'other_credit_long',
    '11': 'other_credit_short',
    '12': 'other_funds_long',
    '13': 'other_funds_short',
    '14': 'other_other_long',
    '15': 'other_other_short',
    '16': 'other_undertakings_long',
    '17': 'other_undertakings_short',
    '18': 'other_directive_long',
    '19': 'other_directive_short',
    '20': 'tot_credit_long',
    '21': 'tot_credit_short',
    '22': 'tot_funds_long',
    '23': 'tot_funds_short',
    '24': 'tot_other_long',
    '25': 'tot_other_short',
    '26': 'tot_undertakings_long',
    '27': 'tot_undertakings_short',
    '28': 'tot_directive_long',
    '29': 'tot_directive_short',
    '30': 'change_commercial_credit_long',
    '31': 'change_commercial_credit_short',
    '32': 'change_commercial_funds_long',
    '33': 'change_commercial_funds_short',
    '34': 'change_commercial_other_long',
    '35': 'change_commercial_other_short',
    '36': 'change_commercial_undertakings_long',
    '37': 'change_commercial_undertakings_short',
    '38': 'change_commercial_directive_long',
    '39': 'change_commercial_directive_short',
    '40': 'change_other_credit_long',
    '41': 'change_other_credit_short',
    '42': 'change_other_funds_long',
    '43': 'change_other_funds_short',
    '44': 'change_other_other_long',
    '45': 'change_other_other_short',
    '46': 'change_other_undertakings_long',
    '47': 'change_other_undertakings_short',
    '48': 'change_other_directive_long',
    '49': 'change_other_directive_short',
    '50': 'change_tot_credit_long',
    '51': 'change_tot_credit_short',
    '52': 'change_tot_funds_long',
    '53': 'change_tot_funds_short',
    '54': 'change_tot_other_long',
    '55': 'change_tot_other_short',
    '56': 'change_tot_undertakings_long',
    '57': 'change_tot_undertakings_short',
    '58': 'change_tot_directive_long',
    '59': 'change_tot_directive_short',
    '60': 'pct_commercial_credit_long',
    '61': 'pct_commercial_credit_short',
    '62': 'pct_commercial_funds_long',
    '63': 'pct_commercial_funds_short',
    '64': 'pct_commercial_other_long',
    '65': 'pct_commercial_other_short',
    '66': 'pct_commercial_undertakings_long',
    '67': 'pct_commercial_undertakings_short',
    '68': 'pct_commercial_directive_long',
    '69': 'pct_commercial_directive_short',
    '70': 'pct_other_credit_long',
    '71': 'pct_other_credit_short',
    '72': 'pct_other_funds_long',
    '73': 'pct_other_funds_short',
    '74': 'pct_other_other_long',
    '75': 'pct_other_other_short',
    '76': 'pct_other_undertakings_long',
    '77': 'pct_other_undertakings_short',
    '78': 'pct_other_directive_long',
    '79': 'pct_other_directive_short',
    '80': 'pct_tot_credit_long',
    '81': 'pct_tot_credit_short',
    '82': 'pct_tot_funds_long',
    '83': 'pct_tot_funds_short',
    '84': 'pct_tot_other_long',
    '85': 'pct_tot_other_short',
    '86': 'pct_tot_undertakings_long',
    '87': 'pct_tot_undertakings_short',
    '88': 'pct_tot_directive_long',
    '89': 'pct_tot_directive_short',
    '90': 'traders_credit',
    '92': 'traders_funds',
    '94': 'traders_other',
    '96': 'traders_undertakings',
    '98': 'traders_directive',
    '100': 'traders_tot_credit',
    '102': 'traders_tot_funds',
    '104': 'traders_tot_other',
    '106': 'traders_tot_undertakings',
    '108': 'traders_tot_directive',
}
