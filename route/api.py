from config.app import *
from .modules import *


# authenticate
api.add_resource(UserLogin,'/login')
api.add_resource(Useregister,'/register')

# webservice
api.add_resource(UserController,'/api/users')
api.add_resource(AbsUserController,'/api/users/<int:_id>')

api.add_resource(OrderController,'/api/order')
api.add_resource(AbsOrderController,'/api/order/<int:_id>')


