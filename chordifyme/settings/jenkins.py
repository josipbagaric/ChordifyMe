from .base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'chordifyme-jenkins',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '',
        'PORT': '',
    }
}

SECRET_KEY = 'dst6@c&qy+nn0)-gu0+$p%$2qk#h6*#mx9%9x)1o3=&jy!2%n8'

