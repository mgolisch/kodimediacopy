import os

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', None)
SQLALCHEMY_BINDS = {
    'kodi':        os.environ.get('KODI_DATABASE_URI', None)
}
SECRET_KEY = os.environ.get('SECRET_KEY', None)
ADMIN_TOKEN = os.environ.get('ADMIN_TOKEN', None)
