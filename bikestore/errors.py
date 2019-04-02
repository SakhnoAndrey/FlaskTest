from flask import render_template
from .application import flask_app, db

@flask_app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@flask_app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500