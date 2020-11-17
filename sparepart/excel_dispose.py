import pandas as pd
import sys
import json


def data_b():
    df = df_pre_dispose()
    dfn = df.groupby([df['o_warehouse_date'].apply(lambda x:x.year)]).agg({'sno':pd.Series.nunique})
    print(dfn)
    return dfn


def data():
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
    temp = ['PFA1','PFA2','PFA3','PFE','PFN','PFY','PFS','PFN','PFH','PFC','PFW']
    df = df[df['asset_no'].isin(temp)]
    return df

def file_pre_dispose():
    df = pd.read_csv("C:/Code/ship-detail20172.csv")
    temp = ['amount','price_per_unit','total_price']
    print(df.info())
    print(df.shape) 
    for t in temp:
        df[t] = df[t].str.replace(',', '')
        df[t] = df[t].str.replace(r'\.00','')
    temp = ['price_per_unit','total_price']
    df.drop(index=df.loc[df['amount'].str.contains(r'\-')].index, inplace=True)
    df.drop(index=df.loc[df['price_per_unit'].str.contains(r'\-')].index, inplace=True)
    df.drop(index=df.loc[df['total_price'].str.contains(r'\-')].index, inplace=True)
    for t in temp:
        df[t] = df[t].astype(float)
    print(df.head())
    print(df.shape)
    df.to_csv('C:/Code/import_db_bak.csv',encoding='utf-8')

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


if __name__ == "__main__" :
    # a = df_pre_dispose()
    a = data_b()
    print(a)