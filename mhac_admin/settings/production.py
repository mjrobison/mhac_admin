from .base import *
from configparser import ConfigParser


DEBUG = False

try:
    from .local import *
except ImportError:
    pass

parser = configparser.ConfigParser()
parser.read("~/db.conf")

SECRET_KEY = parser.get("django", "secrets")
USER = parser.get("DB", "user")
NAME = parser.get("DB", "name")
PASSWORD = parser.get("DB", "password")
HOST = parser.get("DB", "host")
PORT = parser.get("DB", 'port')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': NAME,
        'USER': USER,
        'PASSWORD': PASSWORD,
        'HOST': HOST,
        'PORT': PORT,
    }
}