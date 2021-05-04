from __future__ import absolute_import

from .base import *

SECRET_KEY = "4g%&2hwr@-a2+k=g*9to#3^5p87ft+3f2+n_s&uz)un!%08bog"
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
        "PASSWORD": os.environ.get("DB_PASSWORD", default="VLOzddFcmta2kSSaYcoqKt0zIKwM74YELZnlqNQGTJR7YSgqxLjsqWc9etu8m1fZ"),
        "HOST": os.environ.get("DB_HOST", default="0.0.0.0"),
        "PORT": os.environ.get("DB_PORT", default="5432"),
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
