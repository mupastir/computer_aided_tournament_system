from __future__ import absolute_import

from .base import *

INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
    'rest_framework_swagger',
)

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

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

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# SWAGGER CONF

SWAGGER_SETTINGS = {
        'SECURITY_DEFINITIONS': {
            'api_key': {
                'type': 'apiKey',
                'in': 'header',
                'name': 'Authorization'
            }
        },
        'USE_SESSION_AUTH': False,
    }


LOGIN_URL = 'rest_framework:login'
LOGOUT_URL = 'rest_framework:logout'

if os.environ.get('ENV') == 'behave':
    from .test import *
