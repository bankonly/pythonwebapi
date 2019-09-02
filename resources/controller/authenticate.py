from model.user import UserModel
from werkzeug.security import safe_str_cmp
from flask_restful import Resource,reqparse
from flask_jwt_extended import *
from blacklist import BLACKLIST

parser = reqparse.RequestParser()
parser.add_argument('username',required=True,help="Username is required")
parser.add_argument('password',required=True,help="Password is required")

class UserLogin(Resource):

    def post(self):
        value = parser.parse_args()
        user = UserModel.find_by_name(value.username)
        if user and safe_str_cmp(user.password,value.password):
            accessToken = create_access_token(identity=user.id,fresh=True)
            refreshToken = create_refresh_token(user.id)
            return {
                'accessToken':accessToken,
                'refreshToken':refreshToken,
            }
        return {'msg':'invalid credential'}


class UserRegister(Resource):

    def post(self):
        value = parser.parse_args()
        user = UserModel.find_by_name(value.name)
        if user and safe_str_cmp(user.password,value.password):
            accessToken = create_access_token(identity=user.id,fresh=True)
            refreshToken = create_refresh_token(user.id)
            return {
                'accessToken':accessToken,
                'refreshToken':refreshToken,
            }
        return {'msg':'invalid credential'}

class Logout(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        return BLACKLIST.add(jti)

