# coding: utf-8
from kodimediacopy import db
# generated with https://github.com/ksindi/sqlacodegen


class Actor(db.Model):
    __tablename__ = 'actor'
    __bind_key__ = 'kodi'

    actor_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    art_urls = db.Column(db.Text)


t_actor_link = db.Table(
    'actor_link',
    db.Column('actor_id', db.Integer),
    db.Column('media_id', db.Integer),
    db.Column('media_type', db.Text),
    db.Column('role', db.Text),
    db.Column('cast_order', db.Integer),
    info={'bind_key': 'kodi'}
)


class Art(db.Model):
    __tablename__ = 'art'
    __bind_key__ = 'kodi'

    art_id = db.Column(db.Integer, primary_key=True)
    media_id = db.Column(db.Integer)
    media_type = db.Column(db.Text)
    type = db.Column(db.Text)
    url = db.Column(db.Text)


class Bookmark(db.Model):
    __tablename__ = 'bookmark'
    __bind_key__ = 'kodi'

    idBookmark = db.Column(db.Integer, primary_key=True)
    idFile = db.Column(db.Integer)
    timeInSeconds = db.Column(db.Float(asdecimal=True))
    totalTimeInSeconds = db.Column(db.Float(asdecimal=True))
    thumbNailImage = db.Column(db.Text)
    player = db.Column(db.Text)
    playerState = db.Column(db.Text)
    type = db.Column(db.Integer)


class Country(db.Model):
    __tablename__ = 'country'
    __bind_key__ = 'kodi'

    country_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)


t_country_link = db.Table(
    'country_link',
    db.Column('country_id', db.Integer),
    db.Column('media_id', db.Integer),
    db.Column('media_type', db.Text),
    info={'bind_key': 'kodi'}
)


t_director_link = db.Table(
    'director_link',
    db.Column('actor_id', db.Integer),
    db.Column('media_id', db.Integer),
    db.Column('media_type', db.Text),
    info={'bind_key': 'kodi'}
)


class Episode(db.Model):
    __tablename__ = 'episode'
    __bind_key__ = 'kodi'

    idEpisode = db.Column(db.Integer, primary_key=True)
    idFile = db.Column(db.Integer)
    c00 = db.Column(db.Text)
    c01 = db.Column(db.Text)
    c02 = db.Column(db.Text)
    c03 = db.Column(db.Text)
    c04 = db.Column(db.Text)
    c05 = db.Column(db.Text)
    c06 = db.Column(db.Text)
    c07 = db.Column(db.Text)
    c08 = db.Column(db.Text)
    c09 = db.Column(db.Text)
    c10 = db.Column(db.Text)
    c11 = db.Column(db.Text)
    c12 = db.Column(db.String(24))
    c13 = db.Column(db.String(24))
    c14 = db.Column(db.Text)
    c15 = db.Column(db.Text)
    c16 = db.Column(db.Text)
    c17 = db.Column(db.String(24))
    c18 = db.Column(db.Text)
    c19 = db.Column(db.Text)
    c20 = db.Column(db.Text)
    c21 = db.Column(db.Text)
    c22 = db.Column(db.Text)
    c23 = db.Column(db.Text)
    idShow = db.Column(db.Integer)


t_episode_view = db.Table(
    'episode_view',
    db.Column('idEpisode', db.Integer, server_default=db.FetchedValue()),
    db.Column('idFile', db.Integer),
    db.Column('c00', db.Text),
    db.Column('c01', db.Text),
    db.Column('c02', db.Text),
    db.Column('c03', db.Text),
    db.Column('c04', db.Text),
    db.Column('c05', db.Text),
    db.Column('c06', db.Text),
    db.Column('c07', db.Text),
    db.Column('c08', db.Text),
    db.Column('c09', db.Text),
    db.Column('c10', db.Text),
    db.Column('c11', db.Text),
    db.Column('c12', db.String(24)),
    db.Column('c13', db.String(24)),
    db.Column('c14', db.Text),
    db.Column('c15', db.Text),
    db.Column('c16', db.Text),
    db.Column('c17', db.String(24)),
    db.Column('c18', db.Text),
    db.Column('c19', db.Text),
    db.Column('c20', db.Text),
    db.Column('c21', db.Text),
    db.Column('c22', db.Text),
    db.Column('c23', db.Text),
    db.Column('idShow', db.Integer),
    db.Column('strFileName', db.Text),
    db.Column('strPath', db.Text),
    db.Column('playCount', db.Integer),
    db.Column('lastPlayed', db.Text),
    db.Column('dateAdded', db.Text),
    db.Column('strTitle', db.Text),
    db.Column('studio', db.Text),
    db.Column('premiered', db.Text),
    db.Column('mpaa', db.Text),
    db.Column('resumeTimeInSeconds', db.Float(asdecimal=True)),
    db.Column('totalTimeInSeconds', db.Float(asdecimal=True)),
    db.Column('idSeason', db.Integer, server_default=db.FetchedValue()),
    info={'bind_key': 'kodi'}
)


class File(db.Model):
    __tablename__ = 'files'
    __bind_key__ = 'kodi'

    idFile = db.Column(db.Integer, primary_key=True)
    idPath = db.Column(db.Integer)
    strFilename = db.Column(db.Text)
    playCount = db.Column(db.Integer)
    lastPlayed = db.Column(db.Text)
    dateAdded = db.Column(db.Text)


class Genre(db.Model):
    __tablename__ = 'genre'
    __bind_key__ = 'kodi'

    genre_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)


t_genre_link = db.Table(
    'genre_link',
    db.Column('genre_id', db.Integer),
    db.Column('media_id', db.Integer),
    db.Column('media_type', db.Text),
    info={'bind_key': 'kodi'}
)


class Movie(db.Model):
    __tablename__ = 'movie'
    __bind_key__ = 'kodi'

    idMovie = db.Column(db.Integer, primary_key=True)
    idFile = db.Column(db.Integer)
    c00 = db.Column(db.Text)
    c01 = db.Column(db.Text)
    c02 = db.Column(db.Text)
    c03 = db.Column(db.Text)
    c04 = db.Column(db.Text)
    c05 = db.Column(db.Text)
    c06 = db.Column(db.Text)
    c07 = db.Column(db.Text)
    c08 = db.Column(db.Text)
    c09 = db.Column(db.Text)
    c10 = db.Column(db.Text)
    c11 = db.Column(db.Text)
    c12 = db.Column(db.Text)
    c13 = db.Column(db.Text)
    c14 = db.Column(db.Text)
    c15 = db.Column(db.Text)
    c16 = db.Column(db.Text)
    c17 = db.Column(db.Text)
    c18 = db.Column(db.Text)
    c19 = db.Column(db.Text)
    c20 = db.Column(db.Text)
    c21 = db.Column(db.Text)
    c22 = db.Column(db.Text)
    c23 = db.Column(db.Text)
    idSet = db.Column(db.Integer)


t_movie_view = db.Table(
    'movie_view',
    db.Column('idMovie', db.Integer, server_default=db.FetchedValue()),
    db.Column('idFile', db.Integer),
    db.Column('c00', db.Text),
    db.Column('c01', db.Text),
    db.Column('c02', db.Text),
    db.Column('c03', db.Text),
    db.Column('c04', db.Text),
    db.Column('c05', db.Text),
    db.Column('c06', db.Text),
    db.Column('c07', db.Text),
    db.Column('c08', db.Text),
    db.Column('c09', db.Text),
    db.Column('c10', db.Text),
    db.Column('c11', db.Text),
    db.Column('c12', db.Text),
    db.Column('c13', db.Text),
    db.Column('c14', db.Text),
    db.Column('c15', db.Text),
    db.Column('c16', db.Text),
    db.Column('c17', db.Text),
    db.Column('c18', db.Text),
    db.Column('c19', db.Text),
    db.Column('c20', db.Text),
    db.Column('c21', db.Text),
    db.Column('c22', db.Text),
    db.Column('c23', db.Text),
    db.Column('idSet', db.Integer),
    db.Column('strSet', db.Text),
    db.Column('strFileName', db.Text),
    db.Column('strPath', db.Text),
    db.Column('playCount', db.Integer),
    db.Column('lastPlayed', db.Text),
    db.Column('dateAdded', db.Text),
    db.Column('resumeTimeInSeconds', db.Float(asdecimal=True)),
    db.Column('totalTimeInSeconds', db.Float(asdecimal=True)),
    info={'bind_key': 'kodi'}
)


t_movielinktvshow = db.Table(
    'movielinktvshow',
    db.Column('idMovie', db.Integer),
    db.Column('IdShow', db.Integer),
    info={'bind_key': 'kodi'}
)


class Musicvideo(db.Model):
    __tablename__ = 'musicvideo'
    __bind_key__ = 'kodi'

    idMVideo = db.Column(db.Integer, primary_key=True)
    idFile = db.Column(db.Integer)
    c00 = db.Column(db.Text)
    c01 = db.Column(db.Text)
    c02 = db.Column(db.Text)
    c03 = db.Column(db.Text)
    c04 = db.Column(db.Text)
    c05 = db.Column(db.Text)
    c06 = db.Column(db.Text)
    c07 = db.Column(db.Text)
    c08 = db.Column(db.Text)
    c09 = db.Column(db.Text)
    c10 = db.Column(db.Text)
    c11 = db.Column(db.Text)
    c12 = db.Column(db.Text)
    c13 = db.Column(db.Text)
    c14 = db.Column(db.Text)
    c15 = db.Column(db.Text)
    c16 = db.Column(db.Text)
    c17 = db.Column(db.Text)
    c18 = db.Column(db.Text)
    c19 = db.Column(db.Text)
    c20 = db.Column(db.Text)
    c21 = db.Column(db.Text)
    c22 = db.Column(db.Text)
    c23 = db.Column(db.Text)


t_musicvideo_view = db.Table(
    'musicvideo_view',
    db.Column('idMVideo', db.Integer, server_default=db.FetchedValue()),
    db.Column('idFile', db.Integer),
    db.Column('c00', db.Text),
    db.Column('c01', db.Text),
    db.Column('c02', db.Text),
    db.Column('c03', db.Text),
    db.Column('c04', db.Text),
    db.Column('c05', db.Text),
    db.Column('c06', db.Text),
    db.Column('c07', db.Text),
    db.Column('c08', db.Text),
    db.Column('c09', db.Text),
    db.Column('c10', db.Text),
    db.Column('c11', db.Text),
    db.Column('c12', db.Text),
    db.Column('c13', db.Text),
    db.Column('c14', db.Text),
    db.Column('c15', db.Text),
    db.Column('c16', db.Text),
    db.Column('c17', db.Text),
    db.Column('c18', db.Text),
    db.Column('c19', db.Text),
    db.Column('c20', db.Text),
    db.Column('c21', db.Text),
    db.Column('c22', db.Text),
    db.Column('c23', db.Text),
    db.Column('strFileName', db.Text),
    db.Column('strPath', db.Text),
    db.Column('playCount', db.Integer),
    db.Column('lastPlayed', db.Text),
    db.Column('dateAdded', db.Text),
    db.Column('resumeTimeInSeconds', db.Float(asdecimal=True)),
    db.Column('totalTimeInSeconds', db.Float(asdecimal=True)),
    info={'bind_key': 'kodi'}
)


class Path(db.Model):
    __tablename__ = 'path'
    __bind_key__ = 'kodi'

    idPath = db.Column(db.Integer, primary_key=True)
    strPath = db.Column(db.Text)
    strContent = db.Column(db.Text)
    strScraper = db.Column(db.Text)
    strHash = db.Column(db.Text)
    scanRecursive = db.Column(db.Integer)
    useFolderNames = db.Column(db.Integer)
    strSettings = db.Column(db.Text)
    noUpdate = db.Column(db.Integer)
    exclude = db.Column(db.Integer)
    dateAdded = db.Column(db.Text)
    idParentPath = db.Column(db.Integer)


t_season_view = db.Table(
    'season_view',
    db.Column('idSeason', db.Integer, server_default=db.FetchedValue()),
    db.Column('idShow', db.Integer),
    db.Column('season', db.Integer),
    db.Column('strPath', db.Text),
    db.Column('showTitle', db.Text),
    db.Column('plot', db.Text),
    db.Column('premiered', db.Text),
    db.Column('genre', db.Text),
    db.Column('studio', db.Text),
    db.Column('mpaa', db.Text),
    db.Column('episodes', db.BigInteger, server_default=db.FetchedValue()),
    db.Column('playCount', db.BigInteger, server_default=db.FetchedValue()),
    info={'bind_key': 'kodi'}
)


class Season(db.Model):
    __tablename__ = 'seasons'
    __bind_key__ = 'kodi'

    idSeason = db.Column(db.Integer, primary_key=True)
    idShow = db.Column(db.Integer)
    season = db.Column(db.Integer)


class Set(db.Model):
    __tablename__ = 'sets'
    __bind_key__ = 'kodi'

    idSet = db.Column(db.Integer, primary_key=True)
    strSet = db.Column(db.Text)


t_settings = db.Table(
    'settings',
    db.Column('idFile', db.Integer),
    db.Column('Deinterlace', db.Integer),
    db.Column('ViewMode', db.Integer),
    db.Column('ZoomAmount', db.Float),
    db.Column('PixelRatio', db.Float),
    db.Column('VerticalShift', db.Float),
    db.Column('AudioStream', db.Integer),
    db.Column('SubtitleStream', db.Integer),
    db.Column('SubtitleDelay', db.Float),
    db.Column('SubtitlesOn', db.Integer),
    db.Column('Brightness', db.Float),
    db.Column('Contrast', db.Float),
    db.Column('Gamma', db.Float),
    db.Column('VolumeAmplification', db.Float),
    db.Column('AudioDelay', db.Float),
    db.Column('OutputToAllSpeakers', db.Integer),
    db.Column('ResumeTime', db.Integer),
    db.Column('Sharpness', db.Float),
    db.Column('NoiseReduction', db.Float),
    db.Column('NonLinStretch', db.Integer),
    db.Column('PostProcess', db.Integer),
    db.Column('ScalingMethod', db.Integer),
    db.Column('DeinterlaceMode', db.Integer),
    db.Column('StereoMode', db.Integer),
    db.Column('StereoInvert', db.Integer),
    info={'bind_key': 'kodi'}
)


t_stacktimes = db.Table(
    'stacktimes',
    db.Column('idFile', db.Integer),
    db.Column('times', db.Text),
    info={'bind_key': 'kodi'}
)


t_streamdetails = db.Table(
    'streamdetails',
    db.Column('idFile', db.Integer),
    db.Column('iStreamType', db.Integer),
    db.Column('strVideoCodec', db.Text),
    db.Column('fVideoAspect', db.Float),
    db.Column('iVideoWidth', db.Integer),
    db.Column('iVideoHeight', db.Integer),
    db.Column('strAudioCodec', db.Text),
    db.Column('iAudioChannels', db.Integer),
    db.Column('strAudioLanguage', db.Text),
    db.Column('strSubtitleLanguage', db.Text),
    db.Column('iVideoDuration', db.Integer),
    db.Column('strStereoMode', db.Text),
    info={'bind_key': 'kodi'}
)


class Studio(db.Model):
    __tablename__ = 'studio'
    __bind_key__ = 'kodi'

    studio_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)


t_studio_link = db.Table(
    'studio_link',
    db.Column('studio_id', db.Integer),
    db.Column('media_id', db.Integer),
    db.Column('media_type', db.Text),
    info={'bind_key': 'kodi'}
)


class Tag(db.Model):
    __tablename__ = 'tag'
    __bind_key__ = 'kodi'

    tag_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)


t_tag_link = db.Table(
    'tag_link',
    db.Column('tag_id', db.Integer),
    db.Column('media_id', db.Integer),
    db.Column('media_type', db.Text),
    info={'bind_key': 'kodi'}
)


class Tvshow(db.Model):
    __tablename__ = 'tvshow'
    __bind_key__ = 'kodi'

    idShow = db.Column(db.Integer, primary_key=True)
    c00 = db.Column(db.Text)
    c01 = db.Column(db.Text)
    c02 = db.Column(db.Text)
    c03 = db.Column(db.Text)
    c04 = db.Column(db.Text)
    c05 = db.Column(db.Text)
    c06 = db.Column(db.Text)
    c07 = db.Column(db.Text)
    c08 = db.Column(db.Text)
    c09 = db.Column(db.Text)
    c10 = db.Column(db.Text)
    c11 = db.Column(db.Text)
    c12 = db.Column(db.Text)
    c13 = db.Column(db.Text)
    c14 = db.Column(db.Text)
    c15 = db.Column(db.Text)
    c16 = db.Column(db.Text)
    c17 = db.Column(db.Text)
    c18 = db.Column(db.Text)
    c19 = db.Column(db.Text)
    c20 = db.Column(db.Text)
    c21 = db.Column(db.Text)
    c22 = db.Column(db.Text)
    c23 = db.Column(db.Text)


t_tvshow_view = db.Table(
    'tvshow_view',
    db.Column('idShow', db.Integer, server_default=db.FetchedValue()),
    db.Column('c00', db.Text),
    db.Column('c01', db.Text),
    db.Column('c02', db.Text),
    db.Column('c03', db.Text),
    db.Column('c04', db.Text),
    db.Column('c05', db.Text),
    db.Column('c06', db.Text),
    db.Column('c07', db.Text),
    db.Column('c08', db.Text),
    db.Column('c09', db.Text),
    db.Column('c10', db.Text),
    db.Column('c11', db.Text),
    db.Column('c12', db.Text),
    db.Column('c13', db.Text),
    db.Column('c14', db.Text),
    db.Column('c15', db.Text),
    db.Column('c16', db.Text),
    db.Column('c17', db.Text),
    db.Column('c18', db.Text),
    db.Column('c19', db.Text),
    db.Column('c20', db.Text),
    db.Column('c21', db.Text),
    db.Column('c22', db.Text),
    db.Column('c23', db.Text),
    db.Column('idParentPath', db.Integer),
    db.Column('strPath', db.Text),
    db.Column('dateAdded', db.Text),
    db.Column('lastPlayed', db.Text),
    db.Column('totalCount', db.BigInteger),
    db.Column('watchedcount', db.BigInteger, server_default=db.FetchedValue()),
    db.Column('totalSeasons', db.BigInteger),
    info={'bind_key': 'kodi'}
)


t_tvshowcounts = db.Table(
    'tvshowcounts',
    db.Column('idShow', db.Integer, server_default=db.FetchedValue()),
    db.Column('lastPlayed', db.Text),
    db.Column('totalCount', db.BigInteger),
    db.Column('watchedcount', db.BigInteger, server_default=db.FetchedValue()),
    db.Column('totalSeasons', db.BigInteger),
    db.Column('dateAdded', db.Text),
    info={'bind_key': 'kodi'}
)


t_tvshowlinkpath = db.Table(
    'tvshowlinkpath',
    db.Column('idShow', db.Integer),
    db.Column('idPath', db.Integer),
    info={'bind_key': 'kodi'}
)


t_version = db.Table(
    'version',
    db.Column('idVersion', db.Integer),
    db.Column('iCompressCount', db.Integer),
    info={'bind_key': 'kodi'}
)


t_writer_link = db.Table(
    'writer_link',
    db.Column('actor_id', db.Integer),
    db.Column('media_id', db.Integer),
    db.Column('media_type', db.Text),
    info={'bind_key': 'kodi'}
)
