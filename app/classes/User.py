class User():
    def __init__(self,email):
        __email=email
        __password=None
        __userType=None
        __userName=""
        __authenticate=False
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
    def hash_password(password):
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
    def verify_password(self,email,password):
        result=self.get_user_details(email)
        if(result):
            hashedPassword=hash_password(password)
            if(hashedPassword==self.get_password()):
                self.set_authentication(True)
        else:
            return result




        








    