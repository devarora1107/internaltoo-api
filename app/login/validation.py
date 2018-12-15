import re
import database 
from app.classes.User import User



def validate_usertype(userType):
    try:
        if(int(userType) in [0,1,2]):
            return True
        else:
            return False
    except:
        return False
def validate_email_db(email):   #true means email exist #false email dont
    result=database.get_user_db(email)
    if(result):
        return True
    else:
        return False
def get_user_details(email,password):
    user=database.get_user_db(email)
    if(user):
        user.pop('_id')
        if(user['password']==password):
            user.pop('password')
            user[message]='Login Successful'
            return user
        else:
            return {'message':'Wrong password'}
    else:
        return {'message':"No User Found"}
    
def authenticate_user(email,password):
    user=User(email)
    user.verify_password(password)
    
    
    if(user.get_authentication()):
        
        if(user.create_auth_token()):

            return {
                'message':'login succesfull',
                'status':True,
                'token':user.get_token()
            }
        else:
            return {
                'message':'Login Unsuccesfull',
                'status':False
            }
    else:
        return {
                'message':'Login Unsuccesfull',
                'status':False
                }
    
def create_user(email,password,userType):
    user=User(email)
    if(check_empty_fields(password) and validate_usertype(userType)):
        user.set_password(user.hash_password(password))
        user.set_usertype(userType)
        if(not validate_email_db(user.get_email())):
            user.create_user()
            return {'message':'User Created'}
        else:
            return {'message':'User Already Exist'}
    else:
        return {'message':'Invalid usertype or password'}
