from flask import Blueprint,request,jsonify
from app.login import validation
import json
from bson import json_util, ObjectId
login_blueprint=Blueprint('login',__name__)

@login_blueprint.route('/login',methods=['GET','POST'])
def user_login():
    if(request.method=='POST'):
        data=request.form
        
        if(all(elem in data/keys for elem in ['email','password'])):
            email=data['email']
            password=data['password']
            if(validation.validate_email(email)):
                userDetails=validation.authenticate_user(email,password)
                print userDetails
                return jsonify(userDetails)
                
            else:
                return jsonify({'message':'Invalid Email'})

        else:
            return jsonify({'message':'Incomplete  Data'})
    else:
        return jsonify({'message':'Invalid Method'})


@login_blueprint.route('/signup',methods=['POST'])
def signup_user():
    if(request.method=='POST'):
        data=request.form
        if(all(elem in data.keys()  for elem in ['email','password','userType'] )):
            
            email=data['email']
            if(validation.validate_email(email)):
                password=data['password']
                userType=data['userType']
                userDetails=validation.create_user(email,password,userType)
                return jsonify(userDetails)
            else:
                return jsonify({'message':'Invalid Email'})


        else:
            return jsonify({'message':'Incomplete Data'})
    else:
        return jsonify({'message':'Invalid Method'})