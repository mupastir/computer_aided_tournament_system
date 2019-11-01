from __future__ import absolute_import

from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'oleg',
        'NAME': 'tournament_system',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


DEBUG = True

INSTALLED_APPS += ('behave_django',)
