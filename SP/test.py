import pandas as pd
from datetime import datetime as dt
def delta_month(start_date, end_date):
    start_year = start_date.year
    start_month = start_date.month
    end_year = end_date.year
    end_month = end_date.month
    delta_month = (end_year - start_year) * 12 + (end_month - start_month)
    print(delta_month)
    return delta_month

df = pd.read_csv('./g.csv')
df.set_index('id',inplace=True)
print(df.head())
print(df.info())
print(df['date'].max())
print(df.shape)
print(df.iloc[0,0])



min_year = dt.strptime(df['date'].min(), '%Y-%m')
max_year = dt.strptime(df['date'].max(), '%Y-%m')
start_sno= df.iloc[0,0]


for i in range(0, 100):
    if df.iloc[i, 0] == start_sno:
        delta = delta_month(min_year, df.iloc[i, 1])
        print('current mon：',df.iloc[i,1])
        print('month delta: ',delta)
    else:
        start_sno = df.iloc[i, 0]
        print(start_sno)
    i = i + 1