from flask import Flask
from flask_cors import CORS
from login.login import login_blueprint
app=Flask(__name__)
cors=CORS(app)
app.register_blueprint(login_blueprint)


