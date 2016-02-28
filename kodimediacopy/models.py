import uuid
from kodimediacopy import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    uuid = db.Column(db.String)

    def __init__(self, username):
        self.username = username
        self.uuid = str(uuid.uuid4())

    def __repr__(self):
        return '<User %r>' % self.username


class FileCopy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fileid = db.Column(db.Integer)
    filename = db.Column(db.String)
    filepath = db.Column(db.String)
    type = db.Column(db.String) #tv or movie

    def __repr__(self):
        return '<FileCopy|type:%s|name:%s' % self.type, self.filename


class Posters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String) #tv or movie
    imgdata = db.Column(db.Text) # base64 encoded image data using data-uri notation
    imdbid = db.Column(db.String)
    tvdbid = db.Column(db.String)
