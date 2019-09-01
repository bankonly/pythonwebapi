from model.user import UserModel
from flask_restful import Resource,reqparse
from flask import request as req
from flask_jwt import jwt_required
import json

class UserController(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name',required=True)
    parser.add_argument('email',required=True)
    parser.add_argument('phone',required=True)
    parser.add_argument('password',required=True)

    def post(self):
        value = self.parser.parse_args()
        user = UserModel(**value)
        user.save_to_db()
        return user.json()
    
    @jwt_required()
    def get(self):
        return list(map(lambda l:l.json(), UserModel.query.all())),201


class AbsUserController(UserController):
    
    @jwt_required()
    def get(self,_id):
        users = UserModel.find_by_id(_id)
        if users:
            return users.json()
        return {"msg":'No user'},400
    
    @jwt_required()
    def delete(self,_id):
        users = UserModel.find_by_id(_id)
        if users:
            users.delete_from_db()
            return users.json()
        return {"msg":'No user'},400
    
    @jwt_required()
    def put(self,_id):
        value = self.parser.parse_args()
        users = UserModel.find_by_id(_id)
        if users is not None:
            users.name = value.name
            users.email = value.email
            users.phone = value.phone
            users.password = value.password
            users.save_to_db()
            return users.json()
        return {'msg','no user'},400
    


