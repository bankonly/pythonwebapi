from flask_socketio import *
from .app import *

socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

