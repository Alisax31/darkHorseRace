import pandas as pd
import copy
from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from sparepart import jobs
from sparepart.util import util
from sparepart.dao import dao
from sparepart.data_model import model_fun
from datetime import datetime
from plotly import plot as plt

bp = Blueprint('sp_data_module', __name__)

@bp.route('/test')
def get_data():
    start_year = '2017'
    end_year = '2017'
    # js = dao.get_top5_all_plant_used_sno(start_year)
    jobs.import_data_into_db()
    # print(js)
    return 'success'

@bp.route('/dashboard/scatter/get')
def get_scatter_data():
    js = util.scatter_data()
    return jsonify(js)

@bp.route('/dashboard/keychart/post', methods=['POST'])
def get_keychart_data_all():
    start_year = request.json['start_year']
    end_year = request.json['end_year']
    plants = []
    for item in request.json['plants']:
        tmp = util.plant_agg(item)
        plants.append(tmp)
    sno_type_count = dao.get_sno_type_count(start_year, end_year, plants)
    js = dict()
    js['msg'] = 'success'
    js['percentage'] = sno_type_count[0]
    js['total_amount'] = dao.get_sno_count(start_year, end_year, plants)
    js['total_price'] = dao.get_total_price_count(start_year, end_year, plants)
    # year_gap = int(end_year) - int(start_year)
    # js = {}
    # i = 0
    # while i <= year_gap:
    #     js[str(int(start_year) + i)] = []
    #     i += 1
    # js['msg'] = 'sucess'
    # for item in sno_type_count:
    #     plant = util.plant_split(item[1])
    #     percent = round((int(item[2]) / 10000)*100)
    #     print(type(item[0]))
    #     js[str(item[0])].append({plant: percent})
    return jsonify(js)

@bp.route('/dashboard/keychart/get')
def get_keychart_data():
    temp = dao.get_sno_type_count()
    js = {}
    js_list = []
    js['msg'] = 'sucess'
    for item in temp:
        plant = util.plant_split(item[1])
        percent = round((int(item[2]) / 40000)*100)
        js_list.append({plant: percent})
    js['2017'] = js_list
    return jsonify(js)

# @bp.route('/dashboard/bar/get')
# def get_bar_data():
#     sma_rs = dao.get_sno_month_analysis_data()
#     print(sma_rs)
#     return jsonify(sma_rs)

@bp.route('/dashboard/polar/get')
def get_polar_data():
    js = util.polar_data()
    return jsonify(js)

@bp.route('/dashboard/bar/get')
def get_bar_data_t():
    js = dao.get_top5_sno_data()
    return jsonify(js)

@bp.route('/analysis/timeanalysis/get/<string:sno>')
def get_timeanalysis_data(sno):
    data = dao.get_timeanalysis_data(sno)
    print(data)
    if not data:
        return jsonify({'msg': 'nodata'})
    df = pd.DataFrame(data, columns=['sno','date','sum'])
    df['date'] = df['date'].astype(str)
    train_data = df[0:-1]
    test_data = df[-1:]
    next_month = model_fun.arima_predict(train_data)
    next_month_real = test_data['sum'].values[0]
    print('{} {} 预估 {}, 实际用量{}'.format(sno, test_data.values[0][1], next_month, next_month_real))
    predict = copy.deepcopy(data)
    predict[-1] = [sno, data[-1][1], next_month]
    js = {'msg':'success','actual_value':data,'predict_value':predict}
    return jsonify(js)

@bp.route('/analysis/fbp/get')
def t():
    freq = request.args.get("freq")
    periods = int(request.args.get('periods'))
    sno = request.args.get('sno')
    df = dao.get_fbp_data(sno, freq)
    rs = model_fun.fbp(df, periods, freq)
    rs['msg'] = 'success'
    # rs['ds'] = rs['ds'].strftime('%Y-%m')
    return jsonify(rs)

@bp.route('/dashboard/linechart/get')
def get_line_chart_data():
    temp = dao.get_unused_sno_amount_price()
    df = pd.DataFrame(temp, columns=['year_i','year_o','amount_sum','total_price'])
    df['amount_sum'] = df['amount_sum'].astype(int)
    df['total_price'] = df['total_price'].apply(lambda x: round(x/100000))
    df['amount_sum'] = df['amount_sum'].apply(lambda x: round(x/10000))
    js = df.to_dict(orient='list')
    return jsonify(js)