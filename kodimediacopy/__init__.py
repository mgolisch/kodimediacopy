from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object('kodimediacopy.default_settings')
if app.config['SECRET_KEY'] is None:
    raise Exception('no secret key in config')
if app.config['SQLALCHEMY_DATABASE_URI'] is None:
    raise Exception('app database not configured')
if app.config['SQLALCHEMY_BINDS']['kodi'] is None:
    raise Exception('kodi database not configured')
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

import kodimediacopy.models
import kodimediacopy.views
import kodimediacopy.kodimodels
