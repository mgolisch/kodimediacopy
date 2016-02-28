SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/kodimediacopy.db'
SQLALCHEMY_BINDS = {
    'kodi':        'mysql://kodi:kodi@htpc/MyVideos93'
}
