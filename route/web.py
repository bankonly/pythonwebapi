from .modules import *
from config.app import *
from config.db import Config

Config.db.init_app(app)

# create table
@app.before_first_request
def create_table():
    Config.db.create_all()

@app.route('/me')
@jwt_required
def user():
    user = UserModel.find_by_id(request.users.id)
    return user.json()

@app.route('/')
def home():
    return "Hello world"