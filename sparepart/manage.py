from flask import Blueprint
from sparepart import models
from flask import jsonify
from sparepart import jobs
from flask import current_app
from datetime import datetime
from flask import request
from werkzeug.utils import secure_filename
from sparepart import dao
from os import path

bp = Blueprint('manage', __name__)
@bp.route('/user/get')
def get_user_data():
    aus = models.AuthUser.query.all()
    aus_rs = []
    for au in aus:
        aus_rs.append(au.to_json())     
    # return jsonify(au)
    return jsonify(aus_rs)

@bp.route('/user/delete/<int:uid>')
def delete_user_data(uid):
    flag = dao.delete_user_by_uid(uid)
    if flag:
        return jsonify({'msg':True})
    else: 
        return jsonify({'msg':False})

@bp.route('/user/modify', methods=['POST'])
def modify_user_data():
    if request.method == 'POST':
        email = request.form['email']
        department = request.form['department']
        phone = request.form['phone']
        uid = int(request.form['uid'])
        au = {'uid': uid, 'email': email, 'department': department, 'phone': phone}
        flag = dao.update_user(au)
        if flag:
            return jsonify({'msg':True})
        else:
            return jsonify({'msg':False})
        

@bp.route('/system/job/add', methods=['POST'])
def add_job():
    # result = current_app.apscheduler.add_job(func=jobs.sp_job,id="job1",seconds=10,trigger="interval",replace_existing=True)
    if request.method == 'POST':
        job_name = request.form['jobName']
        func_name = 'sparepart.jobs:' + request.form['funcName']
        args = request.form['args']
        trigger = request.form['trigger']
        interval_date = request.form['intervalDate']
        date_value = request.form['dateValue']
        interval_num = int(request.form['intervalNum'])
        print(func_name)
        if trigger == 'interval':
            if interval_date == 'weeks':
                result = current_app.apscheduler.add_job(func=func_name, id=job_name, weeks=interval_num, trigger=trigger, replace_existing=True)
            elif interval_date == 'days':
                result = current_app.apscheduler.add_job(func=func_name, id=job_name, days=interval_num, trigger=trigger, replace_existing=True)
            elif interval_date == 'hours':
                result = current_app.apscheduler.add_job(func=func_name, id=job_name, hours=interval_num, trigger=trigger, replace_existing=True)
        elif trigger == 'date':
            result = current_app.apscheduler.add_job(func=func_name, id=job_name, hours=interval_date, trigger=trigger, replace_existing=True)
        # print(job_name)
        # print(func_name)
        # print(args)
        # print(trigger)
        # print(interval_date)
        # print(date_value)
        # sparepart.jobs:sp_job
        # if trigger == 'interval':
            # result = current_app.apscheduler.add_job(func=func_name, hours=interval_date, trigger=trigger, replace_existing=True)
    return jsonify({'msg':'success'})

@bp.route('/system/job/remove/<job_id>')
def remove_job(job_id):
    current_app.apscheduler.remove_job(job_id)
    return jsonify({'msg':'success'})

@bp.route('/system/job/pause/<job_id>')
def pause_job(job_id):
    current_app.apscheduler.pause_job(job_id)
    return jsonify({'msg':'success'})

@bp.route('/system/job/resume/<job_id>')
def resume_job(job_id):
    current_app.apscheduler.resume_job(job_id)
    return jsonify({'msg':'success'})

@bp.route('/file/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST' :
       f = request.files['file']
       filename = secure_filename(f.filename)
       temp = filename.split('.')
       base_path = path.dirname(__file__)
       print(base_path)
       abs_path = path.abspath(base_path + '/upload/temp/')
       print(abs_path)
       f.save(abs_path +'/'+ datetime.now().strftime('%Y%m%d%H%M%S') + '.' + temp[-1])
    return jsonify({'msg': 'success'})

@bp.route('/system/msg/get')
def get_msg():
    msg = dao.get_msg_count()
    js = dict()
    js['msg'] =  'success'
    js['msg_count'] = len(msg)
    js['msg_result'] = list()
    for item in msg:
        js['msg_result'].append(item.to_json())
    return jsonify(js)

@bp.route('/system/msg/update')
def update_msg():
    mid = request.args['mid']
    is_read = request.args['is_read']
    js = dao.update_msg(int(mid), int(is_read))
    return jsonify({'msg':'success'})

@bp.route('/test/test')
def job_test():
    jobs.import_data_into_db()
    return "111"