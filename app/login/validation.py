import re
import database 
from app.classes.User import User
def validate_email(email):
    result=re.match("^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",email)
    return result
def validate_mobile_number(number):
    return true

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
                'token':user.get_auth_token()
            }
        else:
            return {
                'message':'Login Unsuccesfull'
            
            }
    else:
        return "oops"