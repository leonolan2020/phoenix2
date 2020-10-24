
import os

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db2.sqlite3',
    }
}


SITE_URL='/phoenix2/'
STATIC_ROOT='/home2/khafonli/public_html/staticfiles/'
MEDIA_ROOT='/home2/khafonli/public_html/media/'

STATIC_URL = SITE_URL+'static/'
MEDIA_URL =  SITE_URL+'media/'

DEBUG=False
# source /home2/khafonli/virtualenv/phoenix2/3.7/bin/activate && cd /home2/khafonli/phoenix2 &&git pull && python manage.py migrate && python manage.py collectstatic --no-input
