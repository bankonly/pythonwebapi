from config.app import *
from config.jwt import *

@app.route('/me')
@jwt_required
def user():
    user = UserModel.find_by_id(request.users.id)
    return user.json()

@app.route('/')
def home():
    return "Hello world"