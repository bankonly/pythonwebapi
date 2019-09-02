from model.user import UserModel
from werkzeug.security import safe_str_cmp
from flask import request
from flask_restful import Resource,reqparse
from flask_jwt_extended import *


parser = reqparse.RequestParser()
parser.add_argument('username',required=True,help="username is required")
parser.add_argument('password',required=True,help="password is required")


class UserLogin(Resource):

    def post(self):
        value = parser.parse_args()
        user = UserModel.find_by_name(value.username)
        if user and safe_str_cmp(user.password,value.password):
            accessToken = create_access_token(identity=user.id,fresh=True)
            refreshToken = create_refresh_token(user.id)
            return {
                'accessToken':accessToken,
                'refreshToken':refreshToken
            }
            
        return {"msg":'invalid credential'}

   
class Useregister(Resource):

    def post(self):
        pass






# def authenticate(username,password):
#     users = UserModel.find_by_name(username)
#     if users and safe_str_cmp(users.password,password):
#         return users
#     return {'msg':'no user'},400

# def identity(payload):
#     users_id = payload['identity']
#     users = UserModel.find_by_id(users_id)
#     request.users = users
#     return users

