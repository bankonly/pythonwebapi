from config.app import *
from config.jwt import *

@app.route('/me')
def user():
    user = UserModel.find_by_id(request.users.id)
    return user.json()

