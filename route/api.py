from .modules import *

# router
api.add_resource(UserController,'/api/users')
api.add_resource(AbsUserController,'/api/users/<int:_id>')

api.add_resource(OrderController,'/api/order')
api.add_resource(AbsOrderController,'/api/order/<int:_id>')


