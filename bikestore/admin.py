from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from .models import User, Post
from .application import flask_app, db

# config for flask-admin
flask_app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(flask_app, name='microblog', template_mode='bootstrap3')

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
