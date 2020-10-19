from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['djangoblogcodigopy.herokuapp.com']
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':  'd9food3c84etq4',
       'USER':  'qcmbcnwvyllvpo',
        'PASSWORD':  '45c1a14c2b08492a88e8a61738c9b7f3336ce472eb0f71aef3d0aa3c621a832f',
        'HOST':'ec2-23-23-242-234.compute-1.amazonaws.com',
        'PORT':5432,
    }
}

STATICFILES_DIRS = (BASE_DIR,'static')