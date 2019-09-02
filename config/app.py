# module
from flask import Flask, request
from flask_restful import Api, Resource
from flask_jwt_extended import *
from resources.controller.authenticate import *



# config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/pythonapi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secretkey'

api = Api(app)

from .jwt import *