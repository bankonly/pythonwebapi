from model.user import UserModel
from werkzeug.security import safe_str_cmp
from flask import request

def authenticate(username,password):
    users = UserModel.find_by_name(username)
    if users and safe_str_cmp(users.password,password):
        return users
    return {'msg':'no user'},400

def identity(payload):
    users_id = payload['identity']
    users = UserModel.find_by_id(users_id)
    request.users = users
    return users

