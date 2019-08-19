from flask_login import LoginManager
from flask_babel import lazy_gettext as _l
from .application import flask_app

login = LoginManager(flask_app)
login.login_view = 'login'
login.login_message = _l('Please log in to access this page.')