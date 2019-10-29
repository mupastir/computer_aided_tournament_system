from .base import *

DATABASES.update({
    'test': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'oleg',
        'NAME': 'tournament_system_test',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
})

INSTALLED_APPS += ('behave_django',)
