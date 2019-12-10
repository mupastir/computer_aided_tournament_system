"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from os.path import abspath, basename, dirname

DJANGO_ROOT = dirname(dirname(abspath(__file__)))
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_ROOT = dirname(DJANGO_ROOT)
BASE_NAME = basename(DJANGO_ROOT)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/


# DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = os.environ.get('DEBUG', default=True)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
# END DEBUG CONFIGURATION

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['*']

# Add custom user model

AUTH_USER_MODEL = 'user_auth.User'

# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
)

LOCAL_APPS = (
    'user_auth.apps.UserAuthConfig',
    'competition.apps.CompetitionConfig',
    'game.apps.GameConfig',
    'participant.apps.ParticipantConfig',
)

THIRD_PART_APPS = (
    'allauth',
    'allauth.account',
    'django_select2',
    'django_celery_results',
    'rest_auth.registration',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'django_countries',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.instagram',
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PART_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '%s.urls' % BASE_NAME

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_ROOT, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

WSGI_APPLICATION = '%s.wsgi.application' % BASE_NAME

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends',
        'USER': '',
        'NAME': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth'
                '.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth'
                '.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth'
                '.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth'
                '.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_ROOT, 'static_base')
STATICFILES_DIRS = [os.path.join(BASE_ROOT, 'static')]

STATIC_URL = '/static/'

# REST Framework

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS':
        'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAdminUser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}

# Internal IPs

INTERNAL_IPS = [
    '127.0.0.1',
]

REST_SESSION_LOGIN = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SITE_ID = 4
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_FORMS = {
    'signup': 'allauth.account.forms.SignupForm',
}
ACCOUNT_LOGOUT_REDIRECT_URL = "/"
LOGIN_REDIRECT_URL = "/"
ACCOUNT_SESSION_REMEMBER = None
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'facebook': {
        'METHOD': 'oauth2',
        'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time',
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.12',
    }
}

# CELERY SETTINGS
CELERY_APP = 'config'
CELERY_BIN = 'celery'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'
CELERY_BROKER_URL = os.environ.get(
    "CELERY_BROKER_URL",
    default='pyamqp://guest@0.0.0.0:5462//')
