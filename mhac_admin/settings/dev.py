from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')k1(9x#$oc(3j5-gc0op_3#d%c5k9*v9wsehi^3y)8y^y_#fs!'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8081',
    'http://localhost:8080',
    'http://localhost:8000',
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8081',
    'http://localhost:8080',
]
try:
    from .local import *
except ImportError:
    pass
