import uuid
from kodimediacopy import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True)
    uuid = db.Column(db.String(250))

    def __init__(self, username):
        self.username = username
        self.uuid = str(uuid.uuid4())

    def __repr__(self):
        return '<User %r>' % self.username


class FileCopy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fileid = db.Column(db.Integer)
    filename = db.Column(db.String(250))
    filepath = db.Column(db.String(250))
    type = db.Column(db.String(50)) #tv or movie
    userid = db.Column(db.Integer,db.ForeignKey('user.id'))
    user = db.relationship('User',backref=db.backref('filecopies',lazy='dynamic')) 
    copied = db.Column(db.Boolean,default=False)

    def __repr__(self):
        return '<FileCopy|type:%s|name:%s>' % (self.type, self.filename)

    def serialize(self):
        return {
            'id':self.id,
            'fileid':self.fileid,
            'filename':self.filename,
            'filepath':self.filepath,
            'type':self.type,
            'userid':self.userid,
            'username':self.user.username,
            'copied':self.copied
        }

class Posters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50)) #tv or movie
    imgdata = db.Column(db.Text(4294967295)) # base64 encoded image data using data-uri notation| force mysql longtext
    apiid = db.Column(db.String(250)) # imdbid|movies or tvdbid|tv , maybe anidbid|anime in future
