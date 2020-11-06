import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db3.sqlite3',
    }
}
ALLOWED_HOSTS = ['127.0.0.1']


SITE_URL='/'
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
STATIC_URL = '/static/'
MEDIA_URL =  '/media/'
DEBUG=True

PUSHER_IS_ENABLE=True