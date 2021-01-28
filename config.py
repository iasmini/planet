import os

# Statement for enabling the development environment
DEBUG = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database SQLite
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.sqlite')
DATABASE_CONNECT_OPTIONS = {}
SECRET_KEY = 'dev'

# FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be
# disabled by default in the future. Set it to True or False to suppress this warning.
SQLALCHEMY_TRACK_MODIFICATIONS = False

ITEMS_PER_PAGE = 10
