from flask_socketio import *
from .app import *
socketio = SocketIO(app)


@socketio.on('connect')
def handleMessage(msg):
    print('Message : ' + msg)
    send(msg,broadcast=True)

