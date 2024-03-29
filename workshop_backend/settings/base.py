"""
Django settings for workshop_backend project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from kavenegar import *


def get_environment_var(var_name, default, prefixed=True):
    if prefixed:
        var_name = 'WORKSHOP_SERVER_%s' % var_name
    return os.getenv(var_name, default)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'workshop_backend.apps.MyAdminConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
    'rest_framework',
    'rest_framework.authtoken',
    'accounts',
    'corsheaders',
    'fsm',
    'scoring',
    'drf_yasg',
    'polymorphic',
    'django_extensions',
    'django_filters',
    'event_metadata',
]

# SITE_ID=1


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# multi-lingual settings below
# LANGUAGES = [
#     ('en', _('English')),
#     ('fa', _('Persian')),
# ]

# USE_I18N = True
#
# USE_L10N = True
#
# LANGUAGE_CODE = 'en'
#
# LOCALE_PATHS = [
#     os.path.join(BASE_DIR, 'locale'),
# ]
# multilingual settings above

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'workshop_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'workshop_backend.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/api/static/'

MEDIA_URL = '/api/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

EMAIL_HOST = 'smtp.zoho.com'
EMAIL_HOST_USER = 'info@rastaiha.ir'
EMAIL_HOST_PASSWORD = 'ET6vmrh.$gHZFjL'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = "Rastaiha <" + EMAIL_HOST_USER + ">"

# Activate Django-Heroku.

OK_STATUS = 'ok'
ERROR_STATUS = 'err'
HELP_STATUS = 'help'

THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (80, 80), 'crop': True},
    },
}

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

CONSTANTS = {
    "PAGINATION_NUMBER": 50,

}

# Custom user model
AUTH_USER_MODEL = "accounts.User"

ASGI_APPLICATION = 'workshop_backend.routing.application'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': '12'
}


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

GUARDIAN_RAISE_403 = True
ANONYMOUS_USER_NAME = None

SWAGGER_SETTINGS = {
    'LOGIN_URL': '/api/auth/accounts/login/',
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
    'DEFAULT_AUTO_SCHEMA_CLASS': 'workshop_backend.settings.custom_setting_classes.CustomAutoSchema',
    'TAGS_SORTER': 'alpha',
    'DOC_EXPANSION': 'none',
}

KAVENEGAR_TOKEN = KavenegarAPI('6A4F554D384477574A7162444F614B4A6C626A64495169306A43417566473655624644394833566C352F593D')

SMS_CODE_DELAY = 5
SMS_CODE_LENGTH = 5

VOUCHER_CODE_LENGTH = 5

DISCOUNT_CODE_LENGTH = 10

PURCHASE_UNIQ_CODE_LENGTH = 10
