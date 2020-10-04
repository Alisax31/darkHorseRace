import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from model_fun import xgBoostReg

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
    df.drop(index=df.loc[df['sum'] > 5000].index, inplace=True)
    df = df.groupby(['sno','date'])['sum'].sum()
    df = df.reset_index()
    # df.drop(index=df.loc[df['sum'] > 1000].index, inplace=True)
    df['date'] = pd.to_datetime(df['date'], format='%Y-%M')
    # df.to_csv('g.csv', encoding='utf-8')
    temp_df = df
    for i in range(df.shape(0)):
        if i == 0:
            t_sno = df['sno'].iloc[0]
            t_date = df['date'].iloc[0]
        elif t_sno != df['sno'].iloc[i] and t_date != df['date'].iloc[i]:
            temp_df.append(pd.DataFrame([df['sno'].iloc[i],df['date'].iloc[i],0], columns=['sno','date','sum']), ignore_index=True)

    return df

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

def describe_data(df):
    print('head:', df.head())
    print('info:', df.info())
    print('describe', df.describe())
    print('skew:', df.skew(axis=0))
    print('kurtosis:', df.kurtosis(axis=0))

if __name__ == '__main__':
    df = import_csv(r'ship-detail20171.csv')
    df = clean_data(df)
    # df = clean_data_new(df)
    # describe_data(df)
    '''
    le = LabelEncoder()
    df['sno'] = le.fit_transform(df['sno'])
    # df['date'] = le.fit_transform(df['date'])
    df['assetno'] =le.fit_transform(df['assetno'])
    df['type'] = le.fit_transform(df['type'])
    #特征值
    print(df.head())
    print(df.corr())
    x = df[['sno','date','assetno','type']]
    #预测值
    y = df['sum']
    #xgboost使用
    #------------------
    #y = y/y.max(axis=0)
    #------------------
    scaler = StandardScaler()
    scaler.fit(x)
    x = scaler.transform(x)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)
    #linearFun(x_train, y_train, x_test, y_test)
    xgBoostReg(x_train, y_train, x_test, y_test)
    # print(dfn.head())
    # print(y_test.head())

    
    # y_test['pred'] = dfn['y_pred']
    # y_test.to_csv('y.csv', encoding='utf-8')
    '''