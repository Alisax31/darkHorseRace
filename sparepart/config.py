from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore 

class Config(object):
    # DEBUG = False
    # TSETING = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://spadmin:SPADMIN@localhost:3306/spadmin"
    # app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://spadmin:SPADMIN@localhost:3306/spadmin"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "1qaz@WSX"
    SQLALCHEMY_POOL_SIZE = "5"
    SQLALCHEMY_POOL_TIMEOUT = "15"
    SCHEDULER_JOBSTORES = {'default': SQLAlchemyJobStore(url=SQLALCHEMY_DATABASE_URI)}
    SCHEDULER_EXECUTORS = {'default': {'type': 'threadpool', 'max_workers': 10}}
    SCHEDULER_API_ENABLED = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql://spadmin:@localhost:3306/spadmin"
    
class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TSETING = True