import pandas as pd
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta

def delta_month(start_date, end_date):
    start_year = start_date.year
    start_month = start_date.month
    end_year = end_date.year
    end_month = end_date.month
    delta_month = (end_year - start_year) * 12 + (end_month - start_month)
    return delta_month

def fill_month_sum(df):
    #df.set_index('id',inplace=True)
    print(type(df['date'].min()))
    print(type(df['date'].max()))
    min_time = dt.strptime(df['date'].min(), '%Y-%m')
    max_time = dt.strptime(df['date'].max(), '%Y-%m')
    start_sno= df.iloc[0,0]
    temp_df = pd.DataFrame(columns=['id','sno','date','sum'])
    for i in range(0, df.shape[0]):
        if df.iloc[i, 0] != start_sno:
            start_sno = df.iloc[i, 0]
            min_time = dt.strptime(df['date'].min(), '%Y-%m')
            if current_time != max_time:
                delta = delta_month(current_time, max_time)
                while delta > 0:
                    next_time = max_time - relativedelta(months=delta-1)
                    # a = {'id':i,'sno':start_sno,'date':next_time,'sum':0}
                    # print(a)
                    temp_df = temp_df.append({'id':i,'sno':start_sno,'date':next_time,'sum':0}, ignore_index = True)
                    delta = delta - 1
        current_time = dt.strptime(df.iloc[i, 1], '%Y-%m')
        delta = delta_month(min_time, current_time)
        if delta > 0:
            while delta > 0:
                next_time = min_time + relativedelta(months=delta-1)
                # a = {'id':i,'sno':start_sno,'date':next_time,'sum':0}
                # print(a)
                temp_df = temp_df.append({'id':i,'sno':start_sno,'date':next_time,'sum':0}, ignore_index = True)
                delta = delta - 1
        # print('sno: ', start_sno)
        # print('current time: ', current_time)
        # print('month delta: ', delta)
        # else:
        #     start_sno = df.iloc[i, 0]
        #     print('start_sno: ', start_sno)
        min_time = current_time + relativedelta(months=1)
        print(i)
        i = i + 1
    # print(temp_df)
    temp_df.to_csv('temp_g.csv', encoding='utf-8')
    return temp_df