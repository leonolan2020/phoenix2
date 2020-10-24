
import os
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-+(&pe9ld9unwos@077r(cg#_)1$^l0c##+%gpy@&95da$=_hp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ON_SERVER_LOCAL=False
ON_SERVER_PARS=False


# ON_SERVER_LOCAL=True
ON_SERVER_PARS=True

ALLOWED_HOSTS = ['127.0.0.1','khafonline.com','www.khafonline.com']


# Application definition

INSTALLED_APPS = [
    'projectmanager',
    'dashboard',
    'authentication',
    'app',
    'app_en',
    'django_cleanup',
    'django_social_share',
    'rest_framework',
    'djecrety',
    'tinymce',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'phoenix2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'dashboard.views.getContext',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'phoenix2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]




if '--no-color' in sys.argv or ON_SERVER_LOCAL:
    ON_SERVER_LOCAL=True  
    ON_SERVER_HEROKU=False
    ON_SERVER_PARS=False


if ON_SERVER_PARS:
    from . import settings_pars as server_settings

if ON_SERVER_LOCAL:
    from . import settings_local as server_settings

DEBUG=server_settings.DEBUG
STATIC_ROOT=server_settings.STATIC_ROOT
MEDIA_ROOT=server_settings.MEDIA_ROOT
STATIC_URL = server_settings.STATIC_URL
MEDIA_URL = server_settings.MEDIA_URL
SITE_URL = server_settings.SITE_URL
DATABASES = server_settings.DATABASES