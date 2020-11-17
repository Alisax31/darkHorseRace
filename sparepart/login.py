from flask import Flask
from flask import Blueprint
from flask import request
from sparepart import models
# from flask import render_template

bp = Blueprint('login', __name__)

@bp.route('/login', methods=['POST'])
def loginValid():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username,password)
        auth_user = models.AuthUser.query.filter_by(username=username).first()
        if auth_user == None:
            return "invalidUser"
        elif auth_user.password != password:
            return "invalidPassword"
        else :
            return "validUser"
