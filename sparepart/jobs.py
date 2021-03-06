# from flask import current_app
import pandas as pd
import shutil
from os import path
from os import listdir
from sparepart.dao import dao
from sparepart import db
from sparepart.util import util
from datetime import datetime
from flask import current_app



def sp_job():
    dao.add_msg("SV000048预测数据")

def sno_month_analysis_model():
    df = dao.get_xgboost_data()
    pass

def import_data_into_db():
    basepath = path.dirname(__file__)
    upload_file_path = basepath + '/upload/temp/'
    filename_list = listdir(upload_file_path)
    if len(filename_list) == 0:
        msg = "此次任务没有找到任何数据文件需要进行导入。"
        dao.add_msg(msg)
        return False
    filename = filename_list[0]
    file_path = upload_file_path + filename
    try:
        df = util.file_pre_dispose(file_path)
        if df is None:
            return False
        row_count = df.shape[0]
        db_engine = ''
        with current_app.app_context():
            app = current_app        
            db_engine = db.get_engine(app=app)
        pd.io.sql.to_sql(df, 'tm_spare_part_all', db_engine, schema="spadmin", if_exists="append", index=False)
        shutil.move(file_path, basepath + upload_success_path + filename)
        msg = filename + '数据处理完毕，成功导入' + str(row_count) + '条，并已经移入已上传目录。'
        dao.add_msg(msg) 
    except OSError as error:
        with current_app.app_context():
            upload_fail_path = current_app.config.get('UPLOAD_FAIL_PATH')
            shutil.move(file_path, basepath + upload_fail_path + filename)
        return None