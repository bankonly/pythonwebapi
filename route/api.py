from config.app import *
from config.jwt import *
from .modules import *


# authenticate
api.add_resource(UserLogin,'/login')
api.add_resource(UserRegister,'/register')
api.add_resource(Logout,'/logout')

# router
api.add_resource(UserController,'/api/users')
api.add_resource(AbsUserController,'/api/users/<int:_id>')

api.add_resource(OrderController,'/api/order')
api.add_resource(AbsOrderController,'/api/order/<int:_id>')


