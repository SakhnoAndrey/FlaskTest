from flask import Flask
from config import Config
from flask_admin import Admin

# config for app
app = Flask(__name__)
app.config.from_object(Config)

from app import routes, models

# config for flask-admin
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, name='microblog', template_mode='bootstrap3')
