from route.api import *
from route.web import *


from config.db import Config
Config.db.init_app(app)


if __name__ == "__main__":
    app.run(port=5000)