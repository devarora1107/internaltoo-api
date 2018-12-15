
import re
def check_empty_fields(data):
    if(data is None or data is ''):

        return False
    else:
        return True

def validate_email(email):
    result=re.match("^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",email)
    return result
def validate_mobile_number(number):
    return true