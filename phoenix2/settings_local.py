import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db2.sqlite3',
    }
}


SITE_URL='/'
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
STATIC_URL = '/static/'
MEDIA_URL =  '/media/'
DEBUG=True