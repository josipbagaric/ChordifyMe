from .base import *

BASE_URL = 'http://localhost:8000'

INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'chordifyme_postgis',
        'PORT': '5432',
    }
}

SECRET_KEY = 'dst6@c&qy+nn0)-gu0+$p%$2qk#h6*#mx9%9x)1o3=&jy!2%n8'