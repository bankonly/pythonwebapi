from .modules import *

@app.route('/me')
@jwt_required()
def user():
    user = UserModel.find_by_id(request.users.id)
    return user.json()