import os

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
STATIC_URL = '/static/'
MEDIA_URL =  '/media/'

DEBUG=True