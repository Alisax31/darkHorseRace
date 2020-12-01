import pandas as pd
import numpy as np
import sys
import json

def polar_data():
    df = df_pre_dispose()
    dfn = df.groupby([df['o_warehouse_date'].apply(lambda x:x.year),'sno'], as_index=False).agg({'asset_no':pd.Series.nunique,'amount':np.sum}).sort_values('sno',ascending=False)
    sno_used_in_all_plant = dfn[dfn['asset_no'] == 10].sort_values('amount',ascending=False).head(5)
    # print(sno_used_in_all_plant)
    top_5_sno_used_in_all_plant = sno_used_in_all_plant['sno'].to_list()
    temp = df[df['sno'].isin(top_5_sno_used_in_all_plant)].groupby([df['o_warehouse_date'].apply(lambda x:x.year), 'sno', 'asset_no'], as_index=False).agg({'amount':np.sum})
    # print(temp)
    # rs = temp.to_dict(orient='list')
    rs = {}
    count = 1
    amount = []
    for item in zip(temp['sno'], temp['amount']):
        if count%10 == 0 :
            amount.append(item[1])
            rs[item[0]] = amount
            amount = []
            count += 1
            continue        
        amount.append(item[1])
        count += 1
        # print('amount: ',amount)
        # print('count: ',count)
    return rs

def temp_data():
    df = df_pre_dispose()
    dfn = df.groupby([df['o_warehouse_date'].apply(lambda x:x.year),'asset_no']).agg({'sno':pd.Series.nunique}).sort_values('sno',ascending=False).head(5)
    dfn.reset_index(inplace=True)
    top5_plant = dfn['asset_no'].to_list()
    df_top5_plant = df[df['asset_no'].isin(top5_plant)]
    df_top5_plant_top3_sno = df_top5_plant.groupby([df['o_warehouse_date'].apply(lambda x:x.year), 'asset_no', 'sno']).agg({'amount':np.sum}).sort_values(by=['asset_no','amount'],ascending=[False,False])
    # print(df_top5_plant_top3_sno)
    df_top5_plant_top3_sno.reset_index(inplace=True)
    rs = []
    for item in top5_plant:
        temp_df = df_top5_plant_top3_sno[df_top5_plant_top3_sno['asset_no'] == item].iloc[0:3]
        rs.append({item : temp_df[['sno','amount']].to_dict(orient='list')})
        # print(temp_df[['sno','amount']].to_dict())
    # print(rs)
    return rs

def scatter_data():
    # dfn = df.groupby([df['o_warehouse_date'].apply(lambda x:x.quarter),'sno','asset_no'])['amount'].sum()#.sort_values('asset_no',ascending=False)
    df = df_pre_dispose()
    dfn = df.groupby(['asset_no',df['o_warehouse_date'].apply(lambda x:x.month)]).agg({'amount':'sum','sno':'count'})
    dfn = dfn.reset_index()
    dfn.sort_values('amount',inplace=True, ascending=False)
    dfn.reset_index(inplace=True)
    dfn.drop('index', axis=1, inplace=True)
    # df.set_index(df['o_warehouse_date']).groupby(pd.TimeGrouper('M')).apply(lambda x:x.groupby(['sno','asset_no']).sum())
    dfnn = dfn.groupby('asset_no')
    result = {}  
    temp = ['PFA1','PFA2','PFA3','PFE','PFN','PFY','PFS','PFN','PFH','PFC','PFW']
    for item in temp:
        dfnn = dfn[dfn['asset_no'] == item]
        dfnn.drop('asset_no', inplace=True, axis=1)
        js = dfnn.to_json(orient='split')
        js = json.loads(js)
        js.pop('index')
        js.pop('columns')
        result[item] = js['data']
    return result

def df_pre_dispose():
    df = pd.read_csv("C:/Code/darkHorseRace/sparepart/upload/temp/import_db_bak.csv", usecols=['sno','asset_no','amount','o_warehouse_date'])
    df['amount'] = df['amount'].astype(int)
    df['o_warehouse_date'] = pd.to_datetime(df['o_warehouse_date'], format='%Y/%m/%d')
    df['asset_no'] = df['asset_no'].str[0:2]
    df['asset_no'] = df['asset_no'].str.upper()
    # df['asset_no'] = df['asset_no'].apply(lambda x:'PFS' if x=='98' else x)
    df['asset_no'] = df['asset_no'].apply(lambda x : plant_split(x))
    temp = ['PFA1','PFA2','PFA3','PFE','PFN','PFY','PFS','PFH','PFC','PFW']
    df = df[df['asset_no'].isin(temp)]
    return df

def file_pre_dispose():
    df = pd.read_csv("C:/Code/2018.xlsx", delimiter='\t')
    temp = ['amount','price_per_unit','total_price']
    for t in temp:
        df[t] = df[t].str.replace(',', '')
        df[t] = df[t].str.replace(r'\.00','')
    temp = ['price_per_unit','total_price']
    df.drop(index=df.loc[df['amount'].str.contains(r'\-')].index, inplace=True)
    df.drop(index=df.loc[df['price_per_unit'].str.contains(r'\-')].index, inplace=True)
    df.drop(index=df.loc[df['total_price'].str.contains(r'\-')].index, inplace=True)
    for t in temp:
        df[t] = df[t].astype(float)
    df.to_csv('C:/Code/import_db_bak_2018.csv',encoding='utf-8')

def plant_split(x):
    if x=='94':
        return 'PFA1'
    elif x=='95':
        return 'PFA2'
    elif x=='97':
        return 'PFA3'
    elif x=='98':
        return 'PFS'
    elif x=='96':
        return 'PFE'
    elif x=='9N':
        return 'PFN'
    elif x=='9Y':
        return 'PFY'
    elif x=='9H':
        return 'PFH'
    elif x=='9C':
        return 'PFC'
    elif x=='9W':
        return 'PFW'
    return x

def plant_agg(x):
    if x=='PFA1':
        return '94'
    elif x=='PFA2':
        return '95'
    elif x=='PFA3':
        return '97'
    elif x=='PFS':
        return '98'
    elif x=='PFE':
        return '96'
    elif x=='PFN':
        return '9N'
    elif x=='PFY':
        return '9Y'
    elif x=='PFH':
        return '9H'
    elif x=='PFC':
        return '9C'
    elif x=='PFW':
        return '9W'
    return x

def share_sno_in_all_plant(df):
    pass


if __name__ == "__main__" :
    file_pre_dispose()
    # a = polar_data()
    # print(a)