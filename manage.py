from flask.ext.script import Manager

from kodimediacopy import app, db
from kodimediacopy.models import User, Posters
from kodimediacopy.kodimodels import Movie, Tvshow
manager = Manager(app)


@manager.option('-n', '--name', dest='name', default='admin')
def adduser(name):
    """
    creates new users
    for each new user a new uuid is generated for login
    """
    print 'adding user %s ' % name
    if User.query.filter_by(username=name).first() is not None:
        print 'user %s exists allready' % name
        return
    user = User(name)
    db.session.add(user)
    db.session.commit()
    print 'user %s created' % name


@manager.option('-n', '--name', dest='name', default=None)
def deleteuser(name):
    """
    delete given user
    """
    if name is None:
        print 'no user specified'
        return

    print 'deleting user %s ' % name
    user = User.query.filter_by(username=name).first()
    if user is None:
        print 'user %s does not exist' % name
        return
    db.session.delete(user)
    db.session.commit()
    print 'user %s deleted' % name


@manager.option('-u', '--url', dest='url', default='http://127.0.0.1:5000/login/')
def listuser(url):
    """
    lists all users in the User table
    including their login url
    param url is the base login url like http://host.tld:port/login/
    """
    print 'listing users:'
    users = User.query.all()
    for user in users:
        print 'name: %s | login_url: %s' % (user.username, url+user.uuid)

@manager.command
def initdb():
    """
    recreate tables from models.py
    bind=None only recreates the tables for the default sqlalchemy connection
    bind based connections are not altered
    ( we dont want sqlalchemy to mess with kodi`s media database)
    """
    db.drop_all(bind=None)
    db.create_all(bind=None)
    adduser('admin')


@manager.command
def updateart():
    import urllib
    from imdbpie import Imdb
    imdb = Imdb()
    print 'updating art for movies(imdb cover)'
    for movie in Movie.query.all():
        print 'processing %s' % movie.c00
        imdbid = movie.c09
        if Posters.query.filter_by(imdbid=imdbid).first() is not None:
            print 'skipping %s as it is allready in the database' % movie.c00
            continue
        title = imdb.get_title_by_id(imdbid)
        if title.cover_url is None:
            continue
        poster = Posters()
        poster.imdbid = imdbid
        poster.type = 'movie'
        response = urllib.urlopen(title.cover_url)
        data = response.read()
        data64 = data.encode('base64').replace('\n', '')
        poster.imgdata = 'data:image/jpeg;base64,%s' % data64
        # print poster.imgdata
        db.session.add(poster)
        db.session.commit()
    print 'updating art for tv'
    from tvdb_api import Tvdb
    t = Tvdb(banners = True)
    for show in Tvshow.query.all():
        print 'processing %s' % show.c00
        tvdbid = show.c12
        if Posters.query.filter_by(tvdbid=tvdbid).first() is not None:
            print 'skipping %s as it is allready in the database' % show.c00 
            continue
        try:
            tvdbshow = t[int(tvdbid)]
            bannerkeys = tvdbshow['_banners']['season']['season'].keys()
            banner_url = tvdbshow['_banners']['season']['season'][bannerkeys[0]]['_bannerpath']
        except:
            continue
        poster = Posters()
        poster.tvdbid = tvdbid
        poster.type = 'tv'
        response = urllib.urlopen(banner_url)
        data = response.read()
        data64 = data.encode('base64').replace('\n', '')
        poster.imgdata = 'data:image/jpeg;base64,%s' % data64
        # print poster.imgdata
        db.session.add(poster)
        db.session.commit()








if __name__ == "__main__":
    manager.run()
