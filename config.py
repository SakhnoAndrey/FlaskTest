import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #    'sqlite:///' + os.path.join(basedir, 'app.db')
    #SQLALCHEMY_DATABASE_URI = 'postgresql://lw:flask@localhost/flask_test'
    SQLALCHEMY_DATABASE_URI = 'postgres://yukfxrte:PkM5ABnQl--7xGWsjH8_yPcwAuxg6tVz@balarama.db.elephantsql.com:5432/yukfxrte'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['andrey.sakhno@gmail.com']
