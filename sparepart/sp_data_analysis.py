from flask import Blueprint
from sparepart import dao
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
# from sparepart import model_fun


bp = Blueprint('sp_data_analysis', __name__)

@bp.route('/analysis/xgboost/get')
def get_xgboost_data():
    rs = dao.get_xgboost_data()
    df =  pd.DataFrame(rs, columns=['sno','date','assetno','sum'])
    le = LabelEncoder()
    df['sno'] = le.fit_transform(df['sno'])
    df['date'] = le.fit_transform(df['date'])
    df['assetno'] =le.fit_transform(df['assetno'])
    # df['type'] = le.fit_transform(df['type'])
    #特征值
    print(df.head())
    print(df.corr())
    x = df[['sno','date','assetno']]
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
    model_fun.xgBoostReg(x_train, y_train, x_test, y_test)
    return "sjsj"