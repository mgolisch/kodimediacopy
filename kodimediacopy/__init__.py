import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask_mail import Mail


app = Flask(__name__)
app.config.from_object('kodimediacopy.default_settings')
if app.config['SECRET_KEY'] is None:
    raise Exception('no secret key in config')
if app.config['SQLALCHEMY_DATABASE_URI'] is None:
    raise Exception('app database not configured')
if app.config['SQLALCHEMY_BINDS']['kodi'] is None:
    raise Exception('kodi database not configured')
#check flask-mail related configs
if app.config['MAIL_SERVER'] is None:
    raise Exception('MAIL_SERVER not configured')
if app.config['MAIL_PORT'] is None:
    raise Exception('MAIL_PORT not configured')
if app.config['MAIL_USERNAME'] is None:
    raise Exception('MAIL_USERNAME not configured')
if app.config['MAIL_PASSWORD'] is None:
    raise Exception('MAIL_PASSWORD not configured')
if app.config['MAIL_DEFAULT_SENDER'] is None:
    raise Exception('MAIL_DEFAULT_SENDER not configured')


db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
mail = Mail(app)

stream_handler = logging.StreamHandler()
app.logger.addHandler(stream_handler)
app.logger.setLevel(logging.INFO)

import kodimediacopy.models
import kodimediacopy.views
import kodimediacopy.kodimodels
