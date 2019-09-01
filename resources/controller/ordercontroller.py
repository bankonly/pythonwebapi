from model.order import OrderModel
from flask_restful import Resource,reqparse
from flask import request as req
from flask_jwt import jwt_required


class OrderController(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('userid',required=True)
    parser.add_argument('menu',required=True,help="menu is reuired")
    parser.add_argument('res',required=True)

    @jwt_required()
    def post(self):

        value = self.parser.parse_args()
        order = OrderModel(**value)
        order.save_to_db()
        return order.json()

    @jwt_required()
    def get(self):
        order = OrderModel.fetch()
        return order.json()

    @jwt_required()
    def get(self):
        return list(map(lambda l:l.json(), OrderModel.query.all())),201


class AbsOrderController(Resource):

    @jwt_required()
    def get(self,_id):
        order = OrderModel.find_by_id(_id)
        if order:
            return order.json()
        return {"msg":'No user'},400

    @jwt_required()
    def delete(self,_id):
        order = OrderModel.find_by_id(_id)
        if order:
            order.delete_from_db()
            return order.json()
        return {"msg":'No user'},400

    @jwt_required()
    def put(self,_id):
        value = self.parser.parse_args()
        order = OrderModel.find_by_id(_id)
        if order is not None:
            order.menu = value['menu']
            order.res = value['res']
            order.userid = value['userid']
            order.save_to_db()
            return order.json()
        return {'msg','no user'},400
    


