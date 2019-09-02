from .app import *
from model.user import UserModel

jwt = JWTManager(app)

@jwt.user_claims_loader
def add_cliams_loader(identity):
    user = UserModel.find_by_id(identity)
    return {
        'id':user.id,
        'name':user.name,
        'phone':user.phone,
        'email':user.email,
        'isadmin':user.isadmin
    }


