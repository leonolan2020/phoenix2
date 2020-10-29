
import os

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'read_default_file': os.path.join(os.path.join(BASE_DIR, 'phoenix2'),'secret_pars.cnf'),

            },
        }
    }
ALLOWED_HOSTS = ['khafonline.com','www.khafonline.com']


SITE_URL='/'
STATIC_ROOT='/home2/khafonli/public_html/phoenix/staticfiles/'
MEDIA_ROOT='/home2/khafonli/public_html/phoenix/media/'
STATIC_URL = SITE_URL+'static/'
MEDIA_URL =  SITE_URL+'media/'
PUSHER_IS_ENABLE=True
DEBUG=False

# source /home2/khafonli/virtualenv/phoenix2/3.7/bin/activate && cd /home2/khafonli/phoenix2 &&git pull && python manage.py migrate && python manage.py collectstatic --no-input
