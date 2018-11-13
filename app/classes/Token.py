class Token():
    def __init__(self,token):
        self.__token=token
        self.__expiryDate=None
        self.__email=None
    

    def get_token(self):
        return self.__token
    def set_token(self,token):
        self.__token=token
    def get_expirydate(self):
        return self.__expiryDate
    def set_expirydate(self,date):
        self.__expiryDate=date
    def get_email(self):
        return self.__email
    def set_email(self,email):
        self.__email=email
    def set_token_headers(self):
        from flask import request
        token=request.headers['X-Access-Token']
        if(token):
            self.set_token(token)
            return True
        else:
            return False
    def decode_token(self):
        from app import app
        import jwt
        try:
            payload = jwt.decode(self.get_token(), app.config.get('SECRET_KEY'))
            self.set_email(payload['sub'])
            self.set_expirydate(payload['exp'])
            return True
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
    def verify_token(self):
        if(self.set_token_headers()):
            pass:
        else:
            return False
        from User import User

        user=User(self.get_email())
        if(user.get_user_details()):
            return user
        else:
            return False




