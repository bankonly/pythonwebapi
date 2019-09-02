from flask_jwt_extended import *
from .app import *
from model.user import *
from blacklist import BLACKLIST
jwt = JWTManager(app)

@jwt.user_claims_loader
def user_claims_loader(identity):
    user = UserModel.find_by_id(identity)
    if user:
        return {
            'id':user.id,
            'name':user.name,
            'email':user.email,
            'phone':user.phone,
            'isadmin':user.isadmin
        }

@jwt.expired_token_loader
def expired_token_loader():
    return {
        'desc':'expired_token_loader'
    },401

@jwt.invalid_token_loader
def invalid_token_loader(err):
    return {
        'desc':'invalid_token_loader'
    },401

@jwt.unauthorized_loader
def unauthorized_loader():
    return {
        'desc':'unauthorized_loader'
    },401

@jwt.revoked_token_loader
def revoked_token_loader():
    return {
        'desc':'revoked_token_loader'
    },401

@jwt.needs_fresh_token_loader
def needs_fresh_token_loader():
    return {
        'desc':'needs_fresh_token_loader'
    },401


@jwt.token_in_blacklist_loader
def check_if_in_blacklist(decryted_token):
    return decryted_token['jti'] in BLACKLIST
