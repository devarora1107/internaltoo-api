
class ExceptionInvalidMethod(Exception):
    def __init__(self):
        self.value={'message':'Invalid Method'}
    def __str__(self):
        return repr(self.value)

class ExceptionIncompleteData(Exception):
    def __init__(self):
        self.value={'message':'Incomplete Data'}
    def __str__(self):
        return repr(self.value)

class ExceptionInvalidEmail(Exception):
    def __init__(self):
        self.value={'message':'Invalid Email'}
    def __self__(self):
        return repr(self.value)