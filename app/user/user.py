from flask import Blueprint,request,jsonify
from app.classes.Token import Token
from app.classes.User import User
user_blueprint=Blueprint('user',__name__)



@user_blueprint.route('/auth/user',methods=['GET'])
def get_user():
    token=request.headers['X-Access-Token']
    token=Token(token)
    token.decode_token()
    user=User(token.get_email())
    user.get_user_details()
    response_data={
        'userName':user.get_username(),
        'userType':user.get_usertype(),
        'access':user.get_access()
    }
    return jsonify(response_data)


# @user_blueprint.route('/createUser')
# def create_user():
#     token=