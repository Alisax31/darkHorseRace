from sparepart import db
from datetime import datetime

class EntityBase(object):
  def to_json(self):
    fields = self.__dict__
    if "_sa_instance_state" in fields:
      del fields["_sa_instance_state"]
    return fields

class AuthUser(db.Model, EntityBase):
  __tablename__ = "auth_user"
  uid = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String('50'), nullable=False)
  email = db.Column(db.String('255'))
  password = db.Column(db.String('32'), nullable=False)
  department = db.Column(db.String('45'))
  phone = db.Column(db.String('45'))
  create_time = db.Column(db.DateTime, default=datetime.now)

class SnoMonthAnalysis(db.Model, EntityBase):
  __tablename__ = "sno_month_analysis"
  id = db.Column(db.Integer, primary_key=True)
  sno = db.Column(db.String('50'))
  consume_date = db.Column(db.DateTime)
  quantity = db.Column(db.Integer)

class TmSparePart(db.Model, EntityBase):
  __tablename__ = "tm_spare_part"
  sid = db.Column(db.Integer, primary_key=True)
  sno = db.Column(db.String(50))
  desc = db.Column(db.String)
  amount = db.Column(db.Integer)
  price_per_unit = db.Column(db.Float)
  total_pric = db.Column(db.Float)
  asset_no = db.Column(db.String(50))
  i_warehouse_date = db.Column(db.DateTime)
  p_type = db.Column(db.String(50))
  o_warehouse_date = db.Column(db.DateTime)