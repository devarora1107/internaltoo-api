from flask import Blueprint,request,jsonify
from app.login import validation
import json
from bson import json_util, ObjectId
login_blueprint=Blueprint('login',__name__)

@login_blueprint.route('/login',methods=['GET','POST'])
def user_login():
    if(request.method=='POST'):
        data=request.form
        
        if('email' and 'password') in data.keys():
            email=data['email']
            password=data['password']
            if(validation.validate_email(email)):
                userDetails=validation.get_user_details(email,password)
                return jsonify(userDetails)
                
            else:
                return jsonify({'message':'Invalid Email'})

        else:
            return jsonify({'message':'Incomplete  Data'})
    else:
        return jsonify({'message':'Invalid Data'})