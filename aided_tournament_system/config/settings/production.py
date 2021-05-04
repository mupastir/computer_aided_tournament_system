from .base import *

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

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", default="*").split(" ")

# Security settings

SECURE_SSL_HOST = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SITE_ID = 1
