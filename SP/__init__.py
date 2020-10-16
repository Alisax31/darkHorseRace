import os
from flask import Flask
from . import index

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev', DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'))
    app.jinja_env.variable_start_string = '[['
    app.jinja_env.variable_end_string = ']]'
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.mkdir(app.instance_path)
    except OSError:
        pass

    # app.register_blueprint(user.bp)
    # app.register_blueprint(wordcloud.bp)
    # app.register_blueprint(examination.bp)
    app.register_blueprint(index.bp)
    # app.add_url_rule('/', endpoint='index')
    return app