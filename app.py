from route.api import *
from config.sokcetio import *
from route.web import *
from blacklist import BLACKLIST
from config.db import Config
Config.db.init_app(app)



# create table
@app.before_first_request
def create_table():
    Config.db.create_all()




if __name__ == "__main__":
    socketio.run(app)