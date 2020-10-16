from flask import Flask
from flask import Blueprint
from flask import render_template

bp = Blueprint('index', __name__)

@bp.route('/index', methods=['GET'])
def index():
    return 'This is Flask App!'