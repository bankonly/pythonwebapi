from config.db import Config
db = Config.db

class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    password = db.Column(db.String(50))

    order = db.relationship('OrderModel',lazy="dynamic")

    def __init__(self,name,email,phone,password):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls,value):
        return cls.query.filter_by(id=value).first()

    @classmethod
    def find_by_name(cls,value):
        return cls.query.filter_by(name=value).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def fetch(cls):
        return cls.query.all()

    def json(self):
        return {
            'id':self.id,
            'name':self.name,
            'email':self.email,
            'phone':self.phone,
            'password':self.password,
            'order':list(map(lambda o:o.json(),self.order.all()))
        }

    