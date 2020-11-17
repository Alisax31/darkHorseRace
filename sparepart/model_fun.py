import xgboost as xgb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.metrics import explained_variance_score

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

