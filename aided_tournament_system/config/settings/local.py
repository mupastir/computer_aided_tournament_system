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

# REST Framework

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS':
        'rest_framework.schemas.coreapi.AutoSchema',

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAdminUser',
    ),
}

# SWAGGER CONF

LOGIN_URL = 'rest_framework:login'
LOGOUT_URL = 'rest_framework:logout'
