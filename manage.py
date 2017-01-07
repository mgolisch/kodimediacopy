import sys, os, shutil, requests
from flask.ext.script import Manager

from kodimediacopy import app, db
from kodimediacopy.models import User, Posters, FileCopy
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
        if Posters.query.filter_by(apiid=imdbid).first() is not None:
            print 'skipping %s as it is allready in the database' % movie.c00
            continue
        try:
            title = imdb.get_title_by_id(imdbid)
            if title.cover_url is None:
                continue
            poster = Posters()
            poster.apiid = imdbid
            poster.type = 'movie'
            response = urllib.urlopen(title.cover_url)
            data = response.read()
            data64 = data.encode('base64').replace('\n', '')
            poster.imgdata = 'data:image/jpeg;base64,%s' % data64
            # print poster.imgdata
            db.session.add(poster)
            db.session.commit()
        except:
            continue
    print 'updating art for tv'
    from tvdb_api import Tvdb
    t = Tvdb(banners = True)
    for show in Tvshow.query.all():
        print 'processing %s' % show.c00
        tvdbid = show.c12
        if Posters.query.filter_by(apiid=tvdbid).first() is not None:
            print 'skipping %s as it is allready in the database' % show.c00
            continue
        try:
            tvdbshow = t[int(tvdbid)]
            bannerkeys = tvdbshow['_banners']['season']['season'].keys()
            banner_url = tvdbshow['_banners']['season']['season'][bannerkeys[0]]['_bannerpath']
            poster = Posters()
            poster.apiid = tvdbid
            poster.type = 'tv'
            response = urllib.urlopen(banner_url)
            data = response.read()
            data64 = data.encode('base64').replace('\n', '')
            poster.imgdata = 'data:image/jpeg;base64,%s' % data64
            # print poster.imgdata
            db.session.add(poster)
            db.session.commit()
        except:
            continue




@manager.option('-d','--directory',dest='directory',default='/mnt/usb/mediacopy/')
def copyfiles(directory):
    for user in User.query.all():
        print 'processing files for user: %s' % user.username
        basepath = os.path.join(directory,user.username)
        if not os.path.exists(basepath):
            os.mkdir(basepath)
        for filecopy in FileCopy.query.filter_by(userid=user.id).all():
            filepath = os.path.join(filecopy.filepath,filecopy.filename)
            print 'copying file: %s' % filepath
            try:
                shutil.copy(filepath,basepath)
            except:
                continue
            filecopy.copied = True
            db.session.add(filecopy)
            db.session.commit()


@manager.option('-d','--directory',dest='directory',default='/mnt/usb/mediacopy/')
@manager.option('-u','--url',dest='url',default='http://127.0.0.1:5000')
def copyfiles_remote(directory,url):
    get_url = url+'/api/filecopy'
    update_url = url+'/api/filecopy/setcopied/'
    if not 'ADMIN_TOKEN' in app.config:
        print 'ADMIN_TOKEN not set.. aborting'
        return
    print 'fetching stuff from %s' % get_url
    response = requests.get(get_url,headers={'auth_token':app.config['ADMIN_TOKEN']})
    if not response.status_code == 200:
        print 'got http status %s .. something went wrong' %response.status_code
        return
    result = response.json()['results']
    for filecopy in result:
        basepath = os.path.join(directory,filecopy['username'])
        if not os.path.exists(basepath):
            os.mkdir(basepath)
        filepath = os.path.join(filecopy['filepath'],filecopy['filename'])
        print 'copying file: %s' % filepath
        try:
            shutil.copy(filepath,basepath)
        except OSError as why:
            print 'error: %s' % why.message
            continue
        requests.get(update_url+str(filecopy['id']),headers={'auth_token':app.config['ADMIN_TOKEN']})

if __name__ == "__main__":
    manager.run()
