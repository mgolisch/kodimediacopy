import os

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', None)
SQLALCHEMY_BINDS = {
    'kodi':        os.environ.get('KODI_DATABASE_URL', None)
}
SECRET_KEY = os.environ.get('SECRET_KEY', None)
ADMIN_TOKEN = os.environ.get('ADMIN_TOKEN', None)

MAIL_SERVER = os.environ.get('MAIL_SERVER', None)
MAIL_PORT = os.environ.get('MAIL_PORT', None)
MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', False)
MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', False)
MAIL_USERNAME = os.environ.get('MAIL_USERNAME', None)
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', None)
MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', None)
