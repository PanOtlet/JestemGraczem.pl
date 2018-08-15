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
    'jestemgraczem.herokuapp.com',
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
    'meta',
    'rest_framework',
    'captcha'
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
    RECAPTCHA_PUBLIC_KEY = os.environ['RECAPTCHA_PUBLIC_KEY']
    RECAPTCHA_PRIVATE_KEY = os.environ['RECAPTCHA_PRIVATE_KEY']
    EMAIL_HOST = os.environ['EMAIL_HOST']
    EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
    EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
    EMAIL_PORT = os.environ['EMAIL_PORT']
    EMAIL_SUBJECT_PREFIX = os.environ['EMAIL_SUBJECT_PREFIX']
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
    EMAIL_HOST = AdminConfig.EMAIL_HOST
    EMAIL_HOST_PASSWORD = AdminConfig.EMAIL_HOST_PASSWORD
    EMAIL_HOST_USER = AdminConfig.EMAIL_HOST_USER
    EMAIL_PORT = AdminConfig.EMAIL_PORT
    EMAIL_SUBJECT_PREFIX = '[JestemGraczem.pl] '
    DEBUG = True
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }

NOCAPTCHA = True

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

if 'TRAVIS' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'travisci',
            'USER': 'postgres',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    DATABASES['default'].update(dj_database_url.config(conn_max_age=500))

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

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = 'home'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Meta datas
meta_description = 'JestemGraczem.pl jest innowacyjną platformą dla graczy! Serwery gier, reklamowanie filmów na YouTube oraz kanałów Streamingowych!'
META = {
    'title': "JestemGraczem.pl",
    'description': meta_description,
    'keywords': [
        'jestemgraczem',
        'jestem graczem',
        'stream',
        'twitch',
        'reklama',
        'promowanie',
        'youtube',
        'jak się wybić',
        'twitch.tv'
    ]
}
