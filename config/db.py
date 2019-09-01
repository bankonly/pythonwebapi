from mysql import connector
from flask_sqlalchemy import SQLAlchemy


class Config:
    dbconnect = connector.connect(host="localhost",user="root",passwd="",database="pythonapi")
    cursor = dbconnect.cursor()
    db = SQLAlchemy()



