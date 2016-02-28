from kodimediacopy import app, db
from kodimediacopy.models import User, Posters
from kodimediacopy.kodimodels import Movie, File, t_streamdetails, Tvshow
from flask import render_template, redirect, session, flash, url_for
from functools import wraps

# helper #


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            flash('not logged in')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function


def build_streaminfo_dict():
    """
    iam using this to build a dict with the information about streams
    """
    class Streaminfo(object):

        def __init__(self, fileid):
            self.filei = fileid
            self.audiostreams = []
            self.videostreams = []
            self.subtilestreams = []

        def add_stream(self ,streaminfo):
            if streaminfo.iStreamType == 0: # video
                self.videostreams.append('res: %sx%s | codec: %s | aspect: %s' % (streaminfo.iVideoWidth, streaminfo.iVideoHeight, streaminfo.strVideoCodec, streaminfo.fVideoAspect))
            if streaminfo.iStreamType == 1: # audio
                self.audiostreams.append('channels: %s | codec: %s | lang: %s' % (streaminfo.iAudioChannels, streaminfo.strAudioCodec,  streaminfo.strAudioLanguage))
            if streaminfo.iStreamType == 2: # subtiles
                self.subtilestreams.append('lang: %s ' % (streaminfo.strSubtitleLanguage))

        def render(self, streams):
            html = '<ul>'
            for stream in streams:
                html += '<li>%s</li>' % stream
            html += '</ul>'
            return html

        def render_video(self):
            return self.render(self.videostreams)

        def render_audio(self):
            return self.render(self.audiostreams)

        def render_subtitle(self):
            return self.render(self.subtilestreams)

    class StreaminfoCollection(object):

        def __init__(self):
            self.col = {}

        def get(self, key):
            if key in self.col:
                return self.col[key]
            else:
                streaminfo = Streaminfo(key)
                self.col[key] = streaminfo
                return streaminfo

    streaminfocollection = StreaminfoCollection()
    streaminfos = db.session.query(t_streamdetails).all() 
    for streaminfo in streaminfos:
        streaminfo_obj = streaminfocollection.get(streaminfo.idFile)
        streaminfo_obj.add_stream(streaminfo)
    return streaminfocollection

# views #


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/<login_uuid>')
def login(login_uuid):
    user = User.query.filter_by(uuid=login_uuid).first()
    if user is None:
        flash("invalid login token")
    else:
        session['logged_in'] = True
        session['user_id'] = user.id
        session['user_name'] = user.username
        flash('logged in')
    return redirect(url_for('index'))


@app.route('/logout')
@login_required
def logout():
    del session['logged_in']
    del session['user_id']
    del session['user_name']
    flash('logged out')
    return redirect(url_for('index'))


@app.route('/movies')
@login_required
def show_movies():
    movies = Movie.query.order_by(Movie.c00).all()
    streaminfo_dict = build_streaminfo_dict()
    posterdict = {poster.imdbid: poster.imgdata for poster in Posters.query.filter_by(type='movie').all()}
    return render_template('movies.html', movies=movies, posters=posterdict, streaminfos=streaminfo_dict)


@app.route('/shows')
@login_required
def show_tv():
    shows = Tvshow.query.order_by(Tvshow.c00).all()
    streaminfo_dict = build_streaminfo_dict()
    posterdict = {poster.tvdbid: poster.imgdata for poster in Posters.query.filter_by(type='tv').all()}
    return render_template('shows.html', shows=shows, posters=posterdict, streaminfos=streaminfo_dict)
    
