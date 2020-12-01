from datetime import datetime
from flask import Flask
from sparepart import models
from flask import Blueprint

bp = Blueprint('index', __name__)
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost:3306/spadmin"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class Auth_user(db.Model):
#   __tablename__ = "auth_user"
#   uid = db.Column(db.Integer, primary_key=True)
#   username = db.Column(db.String('50'), nullable=False)
#   email = db.Column(db.String('255'))
#   password = db.Column(db.String('32'), nullable=False)
#   department = db.Column(db.String('45'))
#   phone = db.Column(db.String('45'))
#   create_time = db.Column(db.DateTime, default=datetime.now)


@bp.route('/<username>/<password>')
def index(username, password):
  auth_user = models.AuthUser(username=username, password=password)
  db.session.add(auth_user)
  db.session.commit()
  return 'Add new user'

@bp.route('/user/<username>')
def get_user(username):
  auth_user = models.AuthUser.query.filter_by(username=username).first()
  print(auth_user)
  return f'The user password is {auth_user.password}'

@bp.route('/indexjsp')
def indexjsp():
  return "index"