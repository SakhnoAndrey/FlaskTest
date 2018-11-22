from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.models import User, Post

# config for app
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

# config for flask-admin
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, name='microblog', template_mode='bootstrap3')

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))