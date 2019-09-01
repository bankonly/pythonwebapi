# module
from flask import Flask,request
from config.db import Config
from flask_restful import Api,Resource
from flask_jwt import JWT,jwt_required
from resources.controller.authenticate import *

# controller
from resources.controller.usercontroller import *
from resources.controller.ordercontroller import *


# config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/pythonapi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secretkey'

api = Api(app)

jwt = JWT(app,authenticate,identity)