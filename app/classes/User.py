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
        __password=password
    def get_usertype(self):
        return self.__userType
    def set_usertype(self,userType):
        __userType=userType
    def get_username(self):
        return self.__userName
    def set_username(self,userName):
        __userName=userName
    def get_authentication(self):
        return self.__authenticate
    def set_authentication(self,authenticate):
        self.__authenticate=authenticate
    def get_token(self):
        return self.__token
    def set_token(self,token):
        __token=token
    
    def hash_password(self,password):
        from passlib.hash import sha256_crypt
        hashedPassword=sha256_crypt.hash(password)
        
        return hashedPassword
    def get_user_details(self,email):
        from app.login import database
        user=database.get_user_db(self.get_email())
        if(user):
            if(('userName' and 'password' and 'userType') in user.keys()):
                self.set_usertype(user['userType'])
                self.set_password(user['password'])
                self.set_username(user['userName'])
                return True
            else:
                return 'Incompelte Data'
        else:
            return 'Not Registerted User'
    def verify_password(self,password):
        result=self.get_user_details(self.get_email())
        print self.hash_password('123456')
        if(result):
            hashedPassword=self.hash_password(password)
            print hashedPassword
            if(hashedPassword==self.get_password()):
                
                self.set_authentication(True)
        else:
            return result

    def create_auth_token(self,):
        
        import jwt
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': self.get_email()
            }
            self.set_token(jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            ))
            return True
        except Exception as e:
            return False
   


        








    