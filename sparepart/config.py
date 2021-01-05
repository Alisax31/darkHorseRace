from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore 

class Config(object):
    # DEBUG = False
    # TSETING = False
    UPLOAD_SUCCESS_PATH = "/upload/uploaded/"
    UPLOAD_FAIL_PATH = "/upload/fail/"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://spadmin:SPADMIN@localhost:3306/spadmin"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SCHEDULER_API_ENABLED = True
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'
    # SCHEDULER_JOBSTORES = {'default': SQLAlchemyJobStore(url=app.config['SQLALCHEMY_DATABASE_URI'])}
    # SECRET_KEY = "1qaz@WSX"
    SQLALCHEMY_POOL_SIZE = "5"
    SQLALCHEMY_POOL_TIMEOUT = "15"
    SCHEDULER_JOBSTORES = {'default': SQLAlchemyJobStore(url=SQLALCHEMY_DATABASE_URI)}
    # SCHEDULER_EXECUTORS = {'default': {'type': 'threadpool', 'max_workers': 10}}

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:svw123@localhost:3306/spadmin"
    
class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TSETING = True