from flask_login import LoginManager
from .application import flask_app

login = LoginManager(flask_app)
login.login_view = 'login'