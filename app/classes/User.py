class User():
    def __init__(self,email):
        self.__email=email
        self.__password=None
        self.__userType=None
        self. __userName=""
        self.__authenticate=False
        self.__token=None
    def get_email(self):
        return self.__email
    def get_password(self):
        return self.__password
    def set_password(self,password):
        self.__password=password
    def get_usertype(self):
        return self.__userType
    def set_usertype(self,userType):
        self.__userType=userType
    def get_username(self):
        return self.__userName
    def set_username(self,userName):
        self. __userName=userName
    def get_authentication(self):
        return self.__authenticate
    def set_authentication(self,authenticate):
        self.__authenticate=authenticate
    def get_token(self):
        return self.__token
    def set_token(self,token):
        self.__token=token
    
    def hash_password(self,password):
        from passlib.hash import sha256_crypt
        hashedPassword=sha256_crypt.hash(password)
        
        return hashedPassword
    def get_user_details(self):
        from app.login import database
        user=database.get_user_db(self.get_email())
        print user
        if(user):
            if(('userName' and 'password' and 'userType') in user.keys()):
                self.set_usertype(int(user['userType']))
                self.set_password(user['password'])
                self.set_username(user['userName'])
                return True
            else:
                return 'Incompelte Data'
        else:
            return 'Not Registerted User'
    def verify_password(self,password):
        from passlib.hash import sha256_crypt
        result=self.get_user_details()
        
        if(result):
            hashedPassword=self.get_password()
            
            if(sha256_crypt.verify(password, hashedPassword)):
                
                self.set_authentication(True)
        else:
            return result

    def create_auth_token(self):
        
        import jwt
        import datetime
        from app import app
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': self.get_email()
        }
        
        self.set_token(jwt.encode(
            payload,
            app.config.get('SECRET_KEY'),
            algorithm='HS256'
        ))
        return True
    def create_user(self):
        from app.login import database
        database.create_user_db({
            'email':self.get_email(),
            'password':self.get_password(),
            'userType':self.get_usertype()
            }
            )
        return 
        
   


        








    