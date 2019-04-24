from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_bootstrap import Bootstrap

# config for app

flask_app = Flask(__name__)
flask_app.config.from_object(Config)
mail = Mail(flask_app)
bootstrap = Bootstrap(flask_app)

db = SQLAlchemy(flask_app)
migrate = Migrate(flask_app, db)
