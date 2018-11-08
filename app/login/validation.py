import re
import database 
def validate_email(email):
    result=re.match("^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",email)
    return result
def validate_mobile_number(number):
    return true

def get_user_details(email,password):
    user=database.get_user_db(email)
    if(user):
        user.pop('_id')
        return user
    else:
        return "No User Found"
    
def check_user_details(email,password=None):
    pass






