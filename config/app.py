# module
from flask import Flask,request
from flask_restful import Api,Resource

# config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://khqfhbmzkhylwi:5bba85cecbd8d8078aa4f6a166c53c45f99915ffded43f723693415d6388b962@ec2-174-129-242-183.compute-1.amazonaws.com:5432/denknjh0vkrfuo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access','refresh']
app.secret_key = 'secretkey'

api = Api(app)

from .jwt import *