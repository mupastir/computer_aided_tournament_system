from __future__ import absolute_import

from .base import *

INSTALLED_APPS += (
    "debug_toolbar",
    "django_extensions",
)

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "USER": os.environ.get("DB_USER", default="oleg"),
        "NAME": os.environ.get("DB_NAME", default="tournament_system"),
        "PASSWORD": os.environ.get("DB_PASSWORD", default=""),
        "HOST": os.environ.get("DB_HOST", default=""),
        "PORT": os.environ.get("DB_PORT", default=""),
    }
}


# SWAGGER CONF

SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "api_key": {"type": "apiKey", "in": "header", "name": "Authorization"}
    },
    "USE_SESSION_AUTH": False,
    "LOGIN_URL": "api_user:login",
    "LOGOUT_URL": "api_user:logout",
}


if os.environ.get("ENV") == "behave":
    from .test import *
