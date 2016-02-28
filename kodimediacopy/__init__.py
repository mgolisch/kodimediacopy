from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('kodimediacopy.default_settings')
app.config.from_pyfile('config.py', silent=True)
if app.config['SECRET_KEY'] is None:
    raise Exception('no secret key in config')
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

import kodimediacopy.models
import kodimediacopy.views
import kodimediacopy.kodimodels
