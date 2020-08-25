create_lme_cotr_table_cmd = """CREATE TABLE IF NOT EXISTS api_lme_cotr (
date DATE NOT NULL,
contract TEXT NOT NULL,
commercial_credit_long FLOAT,
commercial_credit_short FLOAT,
commercial_funds_long FLOAT,
commercial_funds_short FLOAT,
commercial_other_long FLOAT,
commercial_other_short FLOAT,
commercial_undertakings_long FLOAT,
commercial_undertakings_short FLOAT,
commercial_directive_long FLOAT,
commercial_directive_short FLOAT,
other_credit_long FLOAT,
other_credit_short FLOAT,
other_funds_long FLOAT,
other_funds_short FLOAT,
other_other_long FLOAT,
other_other_short FLOAT,
other_undertakings_long FLOAT,
other_undertakings_short FLOAT,
other_directive_long FLOAT,
other_directive_short FLOAT,
tot_credit_long FLOAT,
tot_credit_short FLOAT,
tot_funds_long FLOAT,
tot_funds_short FLOAT,
tot_other_long FLOAT,
tot_other_short FLOAT,
tot_undertakings_long FLOAT,
tot_undertakings_short FLOAT,
tot_directive_long FLOAT,
tot_directive_short FLOAT,
change_commercial_credit_long FLOAT,
change_commercial_credit_short FLOAT,
change_commercial_funds_long FLOAT,
change_commercial_funds_short FLOAT,
change_commercial_other_long FLOAT,
change_commercial_other_short FLOAT,
change_commercial_undertakings_long FLOAT,
change_commercial_undertakings_short FLOAT,
change_commercial_directive_long FLOAT,
change_commercial_directive_short FLOAT,
change_other_credit_long FLOAT,
change_other_credit_short FLOAT,
change_other_funds_long FLOAT,
change_other_funds_short FLOAT,
change_other_other_long FLOAT,
change_other_other_short FLOAT,
change_other_undertakings_long FLOAT,
change_other_undertakings_short FLOAT,
change_other_directive_long FLOAT,
change_other_directive_short FLOAT,
change_tot_credit_long FLOAT,
change_tot_credit_short FLOAT,
change_tot_funds_long FLOAT,
change_tot_funds_short FLOAT,
change_tot_other_long FLOAT,
change_tot_other_short FLOAT,
change_tot_undertakings_long FLOAT,
change_tot_undertakings_short FLOAT,
change_tot_directive_long FLOAT,
change_tot_directive_short FLOAT,
pct_commercial_credit_long FLOAT,
pct_commercial_credit_short FLOAT,
pct_commercial_funds_long FLOAT,
pct_commercial_funds_short FLOAT,
pct_commercial_other_long FLOAT,
pct_commercial_other_short FLOAT,
pct_commercial_undertakings_long FLOAT,
pct_commercial_undertakings_short FLOAT,
pct_commercial_directive_long FLOAT,
pct_commercial_directive_short FLOAT,
pct_other_credit_long FLOAT,
pct_other_credit_short FLOAT,
pct_other_funds_long FLOAT,
pct_other_funds_short FLOAT,
pct_other_other_long FLOAT,
pct_other_other_short FLOAT,
pct_other_undertakings_long FLOAT,
pct_other_undertakings_short FLOAT,
pct_other_directive_long FLOAT,
pct_other_directive_short FLOAT,
pct_tot_credit_long FLOAT,
pct_tot_credit_short FLOAT,
pct_tot_funds_long FLOAT,
pct_tot_funds_short FLOAT,
pct_tot_other_long FLOAT,
pct_tot_other_short FLOAT,
pct_tot_undertakings_long FLOAT,
pct_tot_undertakings_short FLOAT,
pct_tot_directive_long FLOAT,
pct_tot_directive_short FLOAT,
traders_credit TEXT NOT NULL,
traders_funds TEXT NOT NULL,
traders_other TEXT NOT NULL,
traders_undertakings TEXT NOT NULL,
traders_directive TEXT NOT NULL,
traders_tot_credit BIGINT,
traders_tot_funds BIGINT,
traders_tot_other BIGINT,
traders_tot_undertakings BIGINT,
traders_tot_directive TEXT,
PRIMARY KEY (date, Contract));"""
