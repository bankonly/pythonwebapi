from route.api import *
from route.web import *


from config.db import Config
Config.db.init_app(app)

# create table
@app.before_first_request
def create_table():
    Config.db.create_all()

if __name__ == "__main__":
    app.run(port=5000)