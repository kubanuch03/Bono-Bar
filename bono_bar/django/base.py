"""
Django settings for bono_bar project.

Generated by 'django-admin startproject' using Django 4.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
import logging

from bono_bar.env import BASE_DIR, env

logger = logging.getLogger(__name__)

env_path = os.path.join(BASE_DIR, '.env')

if os.path.exists(env_path):
    env.read_env(env_path)
else:
    logger.warning(f".env file not found at {env_path}. Using default environment settings.")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DJANGO_DEBUG", default=True)

ALLOWED_HOSTS = ['*','db']


# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third party apps/services
    'rest_framework',
    'django_redis',
    "drf_yasg",


    # local apps
    'apps.banner',
    'apps.menu',
    'apps.users',
    'apps.category',
    'apps.floors',
    'apps.book',
    'apps.table',
    'apps.wine',
    'apps.gallery',
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bono_bar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'bono_bar.wsgi.application'

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
]

CORS_ALLOWED_ORIGINS = [
    "https://bono-bar.com",
    "http://bono-bar.com",

    "http://localhost:5173",
    "http://localhost:3000",
]

CORS_ALLOW_ORIGINS = [
    "https://bono-bar.com",
    "http://bono-bar.com",
    
    "http://localhost:5173",
    "http://localhost:3000",
]
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

CORS_ALLOW_ALL_ORIGINS = True 


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if env.bool("POSTGRESQL_DATABASE"):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env('POSTGRES_DB'),
            'USER': env('POSTGRES_USER'),
            'PASSWORD': env('POSTGRES_PASSWORD'),
            'HOST': env('POSTGRES_HOST'),
            'PORT': env('POSTGRES_PORT'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': ['redis://localhost:6379/1'],
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",

        }
    }
}

CACHE_TIME = 20

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Bishkek'


USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}

CSRF_USE_SESSIONS = True
CSRF_TRUSTED_ORIGINS = ["https://backend.bono-bar.com"]

# data uploads
DATA_UPLOAD_MAX_MEMORY_SIZE = 104857600  # 100 MB in bytes
FILE_UPLOAD_MAX_MEMORY_SIZE = 104857600  # 100 MB in bytes

EMAIL_BACKEND = env("EMAIL_BACKEND")
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_USE_TLS = env("EMAIL_USE_TLS")

EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")

EMAIL_SERVER = env("EMAIL_SERVER")
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")
EMAIL_ADMIN = env("EMAIL_ADMIN")


CELERY_TIMEZONE = 'Asia/Bishkek'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60

CELERY_BROKER_URL = 'redis://redis:6379/1' 
CELERY_RESULT_BACKEND = 'redis://redis:6379/1'  