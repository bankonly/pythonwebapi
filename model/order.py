from config.db import Config
db = Config.db


class OrderModel(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    menu = db.Column(db.String(50),nullable=False)
    res = db.Column(db.String(50),nullable=False)

    userid = db.Column(db.Integer, db.ForeignKey('users.id'))
    users = db.relationship('UserModel')

    def __init__(self,userid,menu,res):
        self.userid = userid
        self.menu = menu
        self.res = res

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls,value):
        return cls.query.filter_by(id=value).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {
            'userid':self.userid,
            'menu':self.menu,
            'res':self.res
        }