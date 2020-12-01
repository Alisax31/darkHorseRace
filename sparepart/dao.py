import pandas as pd
from sparepart import db
from sparepart import models
from sqlalchemy import func
from sqlalchemy import desc
from sqlalchemy import extract
from sqlalchemy import distinct
# def get_sno_month_analysis_data():
#     SMA = models.SnoMonthAnalysis
#     sma_lists = db.session.query(SMA.sno, func.sum(SMA.quantity).label('sum')).group_by(SMA.sno).order_by(desc('sum')).limit(5).all()
#     # smas = models.SnoMonthAnalysis.query(extract('year', .consume_date).label('year'),func.sum(SnoMonthAnalysis.quantity).label('count')).group_by('year').limit(5).all()
#     sma_rs = []
#     for item in sma_lists:
#         sma_rs.append({'sno':item[0],'sum':int(item[1])})
#     return sma_rs

def get_sno_type_count(start_year, end_year, plants):
    tsp = models.TmSparePart
    temp = db.session.query(func.count(distinct(tsp.sno))).\
    filter(func.upper(func.substr(tsp.asset_no,1,2)).in_(plants), func.year(tsp.o_warehouse_date)>=start_year, func.year(tsp.o_warehouse_date)<=end_year).all()
    return temp[0]

def get_sno_count(start_year, end_year, plants):
    tsp = models.TmSparePart
    temp = db.session.query(func.sum(tsp.amount)).filter(func.upper(func.substr(tsp.asset_no,1,2)).in_(plants), func.year(tsp.o_warehouse_date)>=start_year, func.year(tsp.o_warehouse_date)<=end_year).all()
    return int(temp[0][0])

def get_total_price_count(start_year, end_year, plants):
    tsp = models.TmSparePart
    temp = db.session.query(func.sum(tsp.total_price)).filter(func.upper(func.substr(tsp.asset_no,1,2)).in_(plants), func.year(tsp.o_warehouse_date)>=start_year, func.year(tsp.o_warehouse_date)<=end_year).all()
    return temp[0][0]

def get_top5_sno_data():
    tsp = models.TmSparePart
    temp = db.session.query(tsp.sno,func.year(tsp.o_warehouse_date),func.sum(tsp.amount).label('sum')).group_by(tsp.sno, func.year(tsp.o_warehouse_date)).order_by(desc('sum')).limit(5).all()
    print(temp)
    tsp_rs = []
    for item in temp:
        # print(type(item))
        tsp_rs.append({'sno':item[0], 'sum':int(item[2])})
    return tsp_rs

def get_sno_month_analysis_data():
    sma = models.SnoMonthAnalysis
    sma_list = db.session.query(sma).all()
    return sma_list

def get_xgboost_data():
    tsp = models.TmSparePart
    temp = db.session.query(tsp.sno, func.date_format(tsp.o_warehouse_date, '%Y-%m'), tsp.asset_no, func.sum(tsp.amount).label('sum')).group_by(tsp.sno, func.date_format(tsp.o_warehouse_date, '%Y-%m'), tsp.asset_no).all()
    return temp

def get_timeanalysis_data(sno):
    sma = models.SnoMonthAnalysis
    temp = db.session.query(sma.sno, sma.consume_date, sma.quantity).filter(sma.sno == sno).all()
    sma_list = []
    # print(temp)
    for item in temp:
        print(type(item[1]))
        month = item[1].strftime('%Y-%m')
        print(month)
        sma_list.append([item[0],month,item[2]])
    return sma_list

def get_fbp_data(sno, freq):
    tsp = models.TmSparePart
    if freq == 'Y':
        time_format = '%Y'
    elif freq == 'M':
        time_format = '%Y-%m'
    elif freq == 'D':
        time_format = '%Y-%m-%d'
    temp = db.session.query(tsp.sno, func.date_format(tsp.o_warehouse_date, time_format), func.sum(tsp.amount)).filter(tsp.sno == sno).group_by(tsp.sno, func.date_format(tsp.o_warehouse_date, time_format)).all()
    tsp_list = []
    print(temp)
    for item in temp:
        # day = item[1].strftime(time_format)
        tsp_list.append([item[1], item[2]])
    # print(tsp_list)
    df = pd.DataFrame(tsp_list, columns=['ds','y'])
    # print(df)
    # df.to_csv('C:/Code/fbp.csv')
    return df

def delete_user_by_uid(uid):
    au = models.AuthUser.query.filter_by(uid=uid).first()
    try:
        db.session.delete(au)
        db.session.commit()
        return True
    except:
        return False

def update_user(au):
    au_origin = models.AuthUser.query.filter_by(uid=au['uid']).first()
    au_origin.email = au['email']
    au_origin.department = au['department']
    au_origin.phone = au['phone']
    try:
        db.session.commit()
        return True
    except:
        return False

def add_msg(msg, time):
    tm = models.TmMsg(msg,1)
    db.session.add(tm)
    db.session.commit()
    return True

def get_msg_count():
    tm = models.TmMsg.query.filter_by(is_read=0).all()
    return tm

def update_msg(mid, is_read):
    tm = models.TmMsg.query.filter_by(mid=mid).first()
    tm.is_read = is_read
    try:
        db.session.commit()
        return True
    except:
        return False
