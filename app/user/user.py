from flask import Blueprint,request

user_blueprint=Blueprint('user',__name__)

@user_blueprint.route('/auth/user',methods=['GET'])
def get_user():
    print request.headers['X-Access-Token']
    return jsonify({'hello':'helo'})