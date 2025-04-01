from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
#import os

myapp_obj = Flask(__name__)

myapp_obj.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
myapp_obj.config['SECRET_KEY'] = 'fjgrehfigubhfjlsdhgui56789094567845397y7uhy'
db = SQLAlchemy(myapp_obj)
bcrypt = Bcrypt(myapp_obj)
login_manager = LoginManager(myapp_obj)

from app import routes