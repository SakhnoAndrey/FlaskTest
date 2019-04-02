from bikestore import flask_app
from bikestore.models import User, Post
from bikestore.application import db


@flask_app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


if __name__ == '__main__':
    flask_app.run('127.0.0.1', '5000', debug=False)
