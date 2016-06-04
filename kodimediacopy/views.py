from kodimediacopy import app, db
from kodimediacopy.models import User, Posters, FileCopy
from kodimediacopy.kodimodels import Movie, File, t_streamdetails, Tvshow, Path, t_episode_view
from flask import render_template, redirect, session, flash, url_for, jsonify, abort, request, make_response
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

def api(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not 'auth_token' in request.headers or not 'ADMIN_TOKEN' in app.config or request.headers['auth_token'] != app.config['ADMIN_TOKEN']:
            return make_response(jsonify({'error':'unauthorized'}),401,None)
        return f(*args, **kwargs)
    return decorated_function


def build_streaminfo_dict(list_of_fileids):
    """
    iam using this to build a dict with the information about streams
    """
    class Streaminfo(object):

        def __init__(self, fileid):
            self.fileid = fileid
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
    streaminfos = db.session.query(t_streamdetails).filter(t_streamdetails.c.idFile.in_(list_of_fileids)).all()
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
    userid = session['user_id']
    movies = Movie.query.order_by(Movie.c00).all()
    streaminfo_dict = build_streaminfo_dict([movie.idFile for movie in movies])
    posterdict = {poster.apiid: poster.imgdata for poster in Posters.query.filter_by(type='movie').all()}
    filecopies = {filecopy.fileid: filecopy for filecopy in FileCopy.query.filter_by(userid=userid).all()}
    return render_template('moviesthumb.html', movies=movies, posters=posterdict, streaminfos=streaminfo_dict, filecopies=filecopies)


@app.route('/shows')
@login_required
def show_tv():
    shows = Tvshow.query.order_by(Tvshow.c00).all()
    posterdict = {poster.apiid: poster.imgdata for poster in Posters.query.filter_by(type='tv').all()}
    return render_template('shows.html', shows=shows, posters=posterdict)

@app.route('/shows/<int:id>/episodes')
@login_required
def show_tv_episodes(id):
    userid = session['user_id']
    show = Tvshow.query.filter(Tvshow.idShow == id).first_or_404()
    episodes = db.session.query(t_episode_view).filter(t_episode_view.c.idShow == id).order_by(t_episode_view.c.c12).all()
    streaminfo_dict = build_streaminfo_dict([episode.idFile for episode in episodes])
    filecopies = {filecopy.fileid: filecopy for filecopy in FileCopy.query.filter_by(userid=userid).all()}
    return render_template('shows_episodes.html',  show=show,episodes=episodes, streaminfo_dict=streaminfo_dict,filecopies=filecopies)

@app.route('/movies/add/<string:fileid>')
@login_required
def add_movie(fileid):
    file = File.query.filter_by(idFile=fileid).first()
    path = Path.query.filter_by(idPath=file.idPath).first()
    filecopy = FileCopy()
    filecopy.fileid = fileid
    filecopy.type='movie'
    filecopy.filename = file.strFilename
    filecopy.filepath = path.strPath
    filecopy.userid = session['user_id']
    db.session.add(filecopy)
    db.session.commit()
    flash('marked movie')
    return redirect(url_for('show_movies')+'#'+str(file.idFile))

@app.route('/show/add/episode/<string:episodeid>')
@login_required
def add_episode(episodeid):
    episode = db.session.query(t_episode_view).filter(t_episode_view.c.idEpisode == episodeid).first()
    filecopy = FileCopy()
    filecopy.fileid = episode.idFile
    filecopy.type='show'
    filecopy.filename = episode.strFileName
    filecopy.filepath = episode.strPath
    filecopy.userid = session['user_id']
    db.session.add(filecopy)
    db.session.commit()
    flash('marked episode')
    return redirect(url_for('show_tv_episodes',id=episode.idShow)+'#'+str(episode.idEpisode))

@app.route('/marks')
@login_required
def manage_marks():
    userid = session['user_id']
    filecopies = FileCopy.query.filter(FileCopy.userid == userid).all()
    return render_template('marks.html',filecopies=filecopies)

@app.route('/marks/delete/<int:id>')
@login_required
def delete_mark(id):
    filecopy = FileCopy.query.filter(FileCopy.id==id).first()
    db.session.delete(filecopy)
    db.session.commit()
    return redirect(url_for('manage_marks'))

#remote api for manage.py copyfiles
@app.route('/api/getfilecopies')
@api
def api_get_filecopies():
    return jsonify(results=[filecopy.serialize() for filecopy in  FileCopy.query.all()])

@app.route('/api/filecopy/setcopied/<int:id>')
@api
def api_set_copied(id):
    filecopy = FileCopy.get(id)
    db.session.add(filecopy)
    db.session.commit()
