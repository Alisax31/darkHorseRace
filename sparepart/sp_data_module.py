from flask import Flask
from flask import Blueprint
from flask import request
from sparepart import models
from sparepart import db
from sqlalchemy import func
from sqlalchemy import desc
from sqlalchemy import extract
from sparepart import excel_dispose
from flask import jsonify

bp = Blueprint('sp_data_module', __name__)

@bp.route('/get_sp_dashboard_data')
def get_sp_dashboard_data():
    '''#柱状图代码
    SMA = models.SnoMonthAnalysis
    sma_lists = db.session.query(SMA.sno, func.sum(SMA.quantity).label('sum')).group_by(SMA.sno).order_by(desc('sum')).limit(5).all()
    # smas = models.SnoMonthAnalysis.query(extract('year', .consume_date).label('year'),func.sum(SnoMonthAnalysis.quantity).label('count')).group_by('year').limit(5).all()
    sma_rs = []
    for item in sma_lists:
        sma_rs.append({'sno':item[0],'sum':int(item[1])})
    print(sma_rs)
    return jsonify(sma_rs)
    '''
    js = excel_dispose.data()
    return jsonify(js)