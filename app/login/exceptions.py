class ExceptionWrongPassword(Exception):
    def __init__(self):
        self.value={'message':'Wrong Password'}
    def __self__(self):
        return repr(self.value)