from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
import os
from flask import Flask
from flask_apscheduler import APScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore 
from . import login
from . import manage
from . import sp_data_module
from . import config 

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(SECRET_KEY='dev', DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'))
    app.jinja_env.variable_start_string = '[['
    app.jinja_env.variable_end_string = ']]'
    if test_config is None:
        # app.config.from_object(config.Config())
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.mkdir(app.instance_path)
    except OSError:
        pass
    app.config['UPLOAD_SUCCESS_PATH'] = "/upload/uploaded/"
    app.config['UPLOAD_FAIL_PATH'] = "/upload/fail/"
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://spadmin:SPADMIN@localhost:3306/spadmin"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SCHEDULER_API_ENABLED'] = True
    app.config['SCHEDULER_TIMEZONE'] = 'Asia/Shanghai'
    app.config['SCHEDULER_JOBSTORES'] = {'default': SQLAlchemyJobStore(url=app.config['SQLALCHEMY_DATABASE_URI'])}
    # # db = SQLAlchemy(app)
    # from SP import models
    # db.init_app(app)
    # app.add_url_rule('/', endpoint='index')
    app.register_blueprint(login.bp)
    app.register_blueprint(manage.bp)
    app.register_blueprint(sp_data_module.bp)
    db.init_app(app)
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    return app