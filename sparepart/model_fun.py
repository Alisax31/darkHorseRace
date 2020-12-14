import os
os.environ['OMP_NUM_THREADS'] = "1"
import numpy as np
import pickle
import statsmodels.api as sm
import calendar
import warnings
warnings.filterwarnings("ignore")
# import xgboost as xgb
import pandas as pd
import fbprophet
from itertools import product
from datetime import datetime, timedelta
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.metrics import explained_variance_score
from statsmodels.tsa.arima_model import ARIMA
from fbprophet.diagnostics import cross_validation,performance_metrics




def linearFun(x_train, y_train, x_test, y_test):
    lr = LinearRegression()
    model = lr.fit(x_train, y_train)
    print("模型参数:")
    print(model)
    print("模型截距:")
    print(lr.intercept_)
    print("参数权重:")
    print(lr.coef_)
    y_pred = lr.predict(x_test)
    print('MSE:', metrics.mean_squared_error(y_test, y_pred))
    print('RMSE', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

def xgBoostFun(x_train, y_train,x_test, y_test):
    param = {'boosting_type':'gbdt',
        'objective' : 'reg:linear', #任务类型
        #'objective' : 'regression', #任务类型
        'eval_metric' : 'auc',
        'eta' : 0.01,
        'max_depth' : 19,
        'colsample_bytree':0.8,
        'subsample': 0.9,
        'subsample_freq': 8,
        'alpha': 0.6,
        'lambda': 0,
    }
    train_data = xgb.DMatrix(x_train, label=y_train)
    test_data = xgb.DMatrix(x_test, label=y_test)
    model = xgb.train(param, train_data, evals=[(train_data, 'train'), (test_data, 'valid')], num_boost_round = 10000, early_stopping_rounds=200, verbose_eval=25)
    y_pred = model.predict(test_data)
    print('XGBoost 预测结果', y_pred)
    # print('XGBoost 准确率:', explained_variance_score(y_test,y_pred))

def xgBoostReg(x_train, y_train, x_test, y_test):
    model = xgb.XGBRegressor(n_estimators=150, learning_rate=0.1, gamma=0, max_depth=10)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    print("XGBoost 预测结果统计")
    show_stats(y_pred)
    print('accruace',explained_variance_score(y_test,y_pred))
    # df = pd.DataFrame(y_pred, columns=['y_pred'])
    
def show_stats(data):
    print('min', np.min(data))
    print('max', np.max(data))
    print('ptp', np.ptp(data))
    print('mean', np.mean(data))
    print('std', np.std(data))
    print('var', np.var(data))

def fbp(df, p, freq):
    model = fbprophet.Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=p, freq=freq, include_history=True)
    # future.tail()
    forecast = model.predict(future)
    # model.plot(forecast)
    # model.plot_components(forecast)
    # print(forecast)
    if freq == 'Y':
        time_format = '%Y'
    elif freq == 'M':
        time_format = '%Y-%m'
    elif freq == 'D':
        time_format = '%Y-%m-%d'
    df_cv = cross_validation(model, horizon='30 days')
    df_pe = performance_metrics(df_cv)
    df_cv.to_csv('C:/Users/47135/Desktop/df_cv.csv', encoding='UTF-8')
    df_pe.to_csv('C:/Users/47135/Desktop/df_pe.csv', encoding='UTF-8')
    forecast['ds'] = forecast['ds'].dt.strftime(time_format)
    result = forecast.to_dict(orient='list')
    # print(result)
    return result


def arima_df():
    with open('C:/Code/darkHorseRace/sparepart/data_model/df.pkl', 'rb') as file:
        df = pickle.load(file)
        df = pd.DataFrame(df)
        print(df.head())
    return df

"""
    使用ARIMA时间序列预测下一个月的领用量
    输入：某sno的领用量
    输出：下一个月的预估
"""
def arima_predict(df, verbose=False):
    # 设置参数范围
    ps = range(0, 5)
    qs = range(0, 5)
    ds = range(0, 1)
    parameters = product(ps, ds, qs)
    parameters_list = list(parameters)
    # 寻找最优ARMA模型参数，即best_aic最小
    results = []
    best_aic = float("inf") # 正无穷
    for param in parameters_list:
        try:
            #model = ARIMA(df_month.Price,order=(param[0], param[1], param[2])).fit()
            # SARIMAX 包含季节趋势因素的ARIMA模型
            model = sm.tsa.statespace.SARIMAX(df['sum'],order=(param[0], param[1], param[2]),\
            enforce_stationarity=False,enforce_invertibility=False).fit()
        except ValueError:
            print('参数错误:', param)
            continue
        aic = model.aic
        if aic < best_aic:
            best_model = model
            best_aic = aic
            best_param = param
        results.append([param, model.aic])
    if verbose:
        # 输出最优模型
        print('最优模型: ', best_model.summary())
    # 预测下一个月的领用量
    y_pred = round(best_model.get_prediction(start=len(df)+1, end=len(df)+1).predicted_mean).values[0]
    y_pred_t = round(best_model.get_prediction(start=len(df)+1, end=len(df)+2).predicted_mean).values
    print('y_pred_t: ',y_pred_t)
    print('y_pred_t type:',type(y_pred_t))
    if y_pred < 0:
        y_pred = 0
    # if y_pred_t[0] < 0:
    #     y_pred_t[0] = 0
    # if y_pred_t[1] < 0:
    #     y_pred_t[1] = 0
    return int(y_pred)
    # return y_pred_t

if __name__ == "__main__":
    # df = arima_df()
    # # arima_predict(df,verbose=True)
    # sno_list = "SV000048"
    # temp = df[df['sno'] == sno_list]
    # #print(temp)
    # train_data = temp[0:-1]
    # test_data = temp[-1:]
    # #print('train_data: ', train_data)
    # #print('test_data: ', test_data)
    # next_month = arima_predict(train_data)
    # next_month_real = test_data['sum'].values[0]
    # print('{} {} 预估 {}, 实际用量{}'.format(sno_list, test_data.values[0][1], next_month, next_month_real))
    df = pd.read_csv('C:/Code/fbp.csv')
    a = fbp(df,12)