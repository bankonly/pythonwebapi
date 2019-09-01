from route.api import *
from route.web import *

if __name__ == "__main__":
    from config.db import Config
    Config.db.init_app(app)
    app.run(port=5000)