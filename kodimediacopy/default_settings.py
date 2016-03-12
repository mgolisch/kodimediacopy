from kodimediacopy import app

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/kodimediacopy.db' % app.instance_path # place default sqlitedb in instance folder, can be overidden by instance config
SQLALCHEMY_BINDS = {
    'kodi':        'mysql://kodi:kodi@htpc/MyVideos93'
}
