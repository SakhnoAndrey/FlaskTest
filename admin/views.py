from flask_admin import Admin
from app import app, db
from app.models import User, Post
from flask_admin.contrib.sqla import ModelView

admin = Admin(app, name='microblog', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))