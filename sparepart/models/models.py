from sparepart import db
from datetime import datetime

class EntityBase(object):
    def to_json(self):
        fields = self.__dict__
        if "_sa_instance_state" in fields:
            del fields["_sa_instance_state"]
        return fields

class TmHoliday(db.Model, EntityBase):
    __tablename__ = 'tm_holiday'
    hid = db.Column(db.Integer, primary_key=True)
    holiday_date = db.Column(db.DateTime)

class TmMsg(db.Model, EntityBase):
    __tablename__ = 'tm_msg'
    mid = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text)
    uid = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, default=datetime.now)
    is_read = db.Column(db.Integer, default=0)
    def __init__(self, message, uid, is_read):
        self.message = message
        self.uid = uid
        self.is_read = is_read

class AuthUser(db.Model, EntityBase):
    __tablename__ = "auth_user"
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String('50'), nullable=False)
    email = db.Column(db.String('255'))
    password = db.Column(db.String('32'), nullable=False)
    department = db.Column(db.String('45'))
    phone = db.Column(db.String('45'))
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime)
    def set_attrs(self,attrs_dict):
        for key,value in attrs_dict.items():
            if hasattr(self,key) and key != "uid":
                setattr(self,key,value)

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
    total_price = db.Column(db.Float)
    asset_no = db.Column(db.String(50))
    i_warehouse_date = db.Column(db.DateTime)
    p_type = db.Column(db.String(50))
    o_warehouse_date = db.Column(db.DateTime)

class TmSparePartAll(db.Model, EntityBase):
    __tablename__ = "tm_spare_part_all"
    sid = db.Column(db.Integer, primary_key=True)
    sno = db.Column(db.String(100))
    desc = db.Column(db.String)
    amount = db.Column(db.Integer)
    price_per_unit = db.Column(db.Float)
    total_price = db.Column(db.Float)
    asset_no = db.Column(db.String(50))
    i_warehouse_date = db.Column(db.DateTime)
    p_type = db.Column(db.String(10))
    o_warehouse_date = db.Column(db.DateTime)