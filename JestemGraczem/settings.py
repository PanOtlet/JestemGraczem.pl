import os
import dj_database_url
import urllib.parse
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

ALLOWED_HOSTS = [
    'jestemgraczem.pl',
    'localhost',
    '127.0.0.1',
]

ADMINS = [
    ('otlet', 'otlet@otlet.pl')
]

INSTALLED_APPS = [
    'service.apps.ServiceConfig',
    'stream.apps.StreamConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if not os.path.isfile(BASE_DIR + "/config/config.py"):
    SECRET_KEY = os.environ['SECRET_KEY']
    TWITCH_API_KEY = os.environ['TWITCH_API_KEY']
    YOUTUBE_API_KEY = os.environ['YOUTUBE_API_KEY']
    DEBUG = False
    CACHES = {
        'default': {
            'BACKEND': 'django_bmemcached.memcached.BMemcached',
            'LOCATION': os.environ.get('MEMCACHEDCLOUD_SERVERS').split(','),
            'OPTIONS': {
                'username': os.environ.get('MEMCACHEDCLOUD_USERNAME'),
                'password': os.environ.get('MEMCACHEDCLOUD_PASSWORD')
            }
        }
    }
else:
    from config.config import AdminConfig

    SECRET_KEY = AdminConfig.SECRET_KEY
    TWITCH_API_KEY = AdminConfig.TWITCH_API_KEY
    YOUTUBE_API_KEY = AdminConfig.YOUTUBE_API_KEY
    DEBUG = True
    # CACHES = {
    #     'default': {
    #         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
    #         'LOCATION': os.path.join(BASE_DIR, 'cache').replace('\\', '/'),
    #         'TIMEOUT': 600,
    #         'OPTIONS': {
    #             'MAX_ENTRIES': 1000
    #         }
    #     }
    # }

ROOT_URLCONF = 'JestemGraczem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR + '/templates/',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'service.custom_template_variable.settings_processor'
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'JestemGraczem.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}

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

LANGUAGE_CODE = 'pl-pl'
TIME_ZONE = 'Europe/Warsaw'
USE_I18N = True
USE_L10N = True
USE_TZ = True

DATABASES['default'].update(dj_database_url.config(conn_max_age=500))

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = 'home'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
