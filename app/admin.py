from app.models import User, Post
from app import admin
from app.application import db
from flask_admin.contrib.sqla import ModelView

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
