"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from os.path import abspath, dirname, basename

from django.core.wsgi import get_wsgi_application

DJANGO_ROOT = dirname(dirname(abspath(__file__)))
BASE_NAME = basename(DJANGO_ROOT)
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      '%s.settings.production' % BASE_NAME)

application = get_wsgi_application()
