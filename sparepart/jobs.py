# from flask import current_app
import pandas as pd
import shutil
from os import path
from os import listdir
from sparepart import dao
from sparepart import db
from sparepart import excel_dispose
from datetime import datetime
from flask import current_app



def sp_job():
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    dao.add_msg("SV000048预测数据")

def sno_month_analysis_model():
    df = dao.get_xgboost_data()
    print(df)
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
        df = excel_dispose.file_pre_dispose(file_path)
        if df is None:
            return False
        row_count = df.shape[0]
        db_config = current_app.config.get('SQLALCHEMY_DATABASE_URI')
        upload_success_path = current_app.config.get('UPLOAD_SUCCESS_PATH')
        db_engine = ''
        with current_app.app_context():
            app = current_app        
            db_engine = db.get_engine(app=app)
        pd.io.sql.to_sql(df, 'tm_spare_part_all', db_engine, schema="spadmin", if_exists="append", index=False)
        shutil.move(file_path, basepath + upload_success_path + filename)
        msg = filename + '数据处理完毕，成功导入' + str(row_count) + '条，并已经移入已上传目录。'
        dao.add_msg(msg) 
    except OSError as error:
        print(error)
        with current_app.app_context():
            upload_fail_path = current_app.config.get('UPLOAD_FAIL_PATH')
            shutil.move(file_path, basepath + upload_fail_path + filename)
        return None