# from flask import current_app
from datetime import datetime
import pandas as pd
import numpy as np
# from matplotlib import pyplot as plt
# from sklearn.preprocessing import LabelEncoder
# from sklearn.preprocessing import StandardScaler
# from sklearn.model_selection import train_test_split
# from model_fun import xgBoostReg

def sp_job():
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
'''
def import_csv(path):
    df = pd.read_csv(path, encoding='utf-8')
    # print(df.head())
    return df
def clean_data(df):
    df = df[['物料号','日期','成本中心','数量','申购类型']]
    df = df.rename(columns={'物料号':'sno','日期':'date','成本中心':'assetno','数量':'sum','申购类型':'type'})
    # df_lx = df.loc[df['type'] == '零星']
    # df_bk = df.loc[df['type'] == '补库']    
    df_sv = df.loc[df['sno'].str.startswith('SV')]
    df_tv = df.loc[df['sno'].str.startswith('TV')]
    df = pd.concat([df_sv, df_tv], axis=0)
    df['date'] = pd.to_datetime(df['date'], format='%Y/%m/%d')
    df['date'] = df['date'].map(lambda x:x.strftime('%Y-%m'))
    df['sum'] = df['sum'].str.replace(',','')
    df['sum'] = df['sum'].str.replace('.00','')
    df.drop(index=df.loc[df['sum'].str.match(r"\D")].index, inplace=True)
    df.drop(index=df.loc[df['sum'] == ''].index, inplace=True)
    df.drop(index=df.loc[df['sum'].str.contains(r'\.')].index, inplace=True)
    df.drop(index=df.loc[df['sno'] == 'SV200946'].index, inplace=True)
    df.drop(index=df.loc[df['sum'] == '0'].index, inplace=True)
    df['sum'] = df['sum'].astype(int)
    df.drop(index=df.loc[df['sum'] > 1000].index, inplace=True)
    df = df.groupby(['sno','date'])['sum'].sum()
    df = df.reset_index()
    # df['date'] = pd.to_datetime(df['date'], format='%Y-%M')
    # df.to_csv('g.csv', encoding='utf-8')
    temp_df = spm.fill_month_sum(df)
    # print(temp_df.head())
    # print(df.shape)
    return temp_df

def clean_data_new(df):
    # df = df[['物料号','日期','成本中心','数量','申购类型']]
    df = df.rename(columns={'物料号':'sno','日期':'date','成本中心':'assetno','数量':'sum','申购类型':'type'})
    print(df.shape)
    df['type'] = df['type'].str.replace(' ','')
    df.drop(index=df.loc[df['type'] == ''].index, inplace=True)
    df.drop(index=df.loc[df['sum'].str.match(r"\D")].index, inplace=True)
    df.drop(index=df.loc[df['sum'] == ''].index, inplace=True)
    df.drop(index=df.loc[df['sum'].str.contains(r'\.')].index, inplace=True)
    df.drop(index=df.loc[df['sno'] == 'SV200946'].index, inplace=True)
    df.drop(index=df.loc[df['sum'] == '0'].index, inplace=True)
    df_sv = df.loc[df['sno'].str.startswith('SV')]
    df_tv = df.loc[df['sno'].str.startswith('TV')]
    df = pd.concat([df_sv, df_tv], axis=0)
    df['date'] = pd.to_datetime(df['date'], format='%Y/%M/%d')
    df['date'] = df['date'].map(lambda x:x.strftime('%Y%M%d'))
    df['assetno'] = df['assetno'].str.upper()
    df['sum'] = df['sum'].astype(int)
    print(df.shape)
    return df[['sno','date','assetno','type','sum']]
'''