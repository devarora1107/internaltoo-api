from flask import Flask
from flask_cors import CORS
from login.login import login_blueprint
app=Flask(__name__)
app.config['SECRET_KEY']='&X\x10\xd0\x02\x19\xaa9\x14+j\xea\x97\xadj\xe0\xc1\x18\x9a\xb7#\xf0\x84?\x81\xea'
cors=CORS(app)
app.register_blueprint(login_blueprint)



