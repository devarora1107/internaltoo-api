from flask import Blueprint,request,jsonify,Response
import validation

from bson import json_util, ObjectId
from app.exceptions.commonException import ExceptionInvalidMethod,ExceptionIncompleteData,ExceptionInvalidEmail

from exceptions import ExceptionWrongPassword
from app.validation import commonValidation
login_blueprint=Blueprint('login',__name__)
#to login user
@login_blueprint.route('/auth/login',methods=['GET','POST'])
def user_login():
    try:
        if(request.method=='POST'):
            data=request.json
            print request.json
            #data={'email':'devarora2@outlook.com','password':'123456'}
            if(all(elem in data.keys() for elem in ['email','password'])):
                email=data['email']
                password=data['password']
                if(commonValidation.validate_email(email)):
                    userDetails=validation.authenticate_user(email,password)
                    if(userDetails['status']):
                        return jsonify(userDetails),200
                    else:
                        raise ExceptionWrongPassword

                
                    
                else:
                    raise ExceptionInvalidEmail

            else:
                raise ExceptionIncompleteData
        else:
            raise ExceptionInvalidMethod

    
    except ExceptionInvalidMethod as e:
        return jsonify(e.value),405
    except ExceptionIncompleteData as e:
        return jsonify(e.value),422
    except ExceptionInvalidEmail as e:
        return jsonify(e.value),422
    except ExceptionWrongPassword as e:
        return jsonify(e.value),401
    
        
#to signup user

@login_blueprint.route('/signup',methods=['POST','GET'])
def signup_user():
    try:
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
                    raise ExceptionInvalidEmail


            else:
                raise ExceptionIncompleteData
        else:
            raise ExceptionInvalidMethod
    except ExceptionInvalidMethod as e:
        return jsonify(e.value)
    except ExceptionIncompleteData as e:
        return jsonify(e.value)
    except ExceptionInvalidEmail as e:
        return jsonify(e.value)
#for registration user
@login_blueprint.route('/registration',methods=['POST'])
def registration():
    if(request.method=='POST'):
        data=request.form
    else:
        return {'message':'sdasd'}

