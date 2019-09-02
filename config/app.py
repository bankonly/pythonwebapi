# module
from flask import *
from flask_restful import Api,Resource
from flask_cors import *
# config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://khqfhbmzkhylwi:5bba85cecbd8d8078aa4f6a166c53c45f99915ffded43f723693415d6388b962@ec2-174-129-242-183.compute-1.amazonaws.com:5432/denknjh0vkrfuo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access','refresh']
app.config['SECRET_KEY'] ='89fhrfw-89refhns9ueasdasda'
app.config['CORS_HEADERS'] = 'Content-Type'
# app.secret_key = '89fhrfw-89refhns9ueasdasda'

api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})