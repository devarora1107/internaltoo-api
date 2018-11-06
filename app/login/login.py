from flask import Blueprint

login_blueprint=Blueprint('login',__name__)

@login_blueprint.route('/login',method=['GET','POST'])
def user_login():
    data=request.form
    if('email' and 'password') in data.keys():


    else:
        return 'Invalid Data'