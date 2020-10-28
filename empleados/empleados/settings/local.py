from .base import *

DEBUG = True

ALLOWED_HOSTS = []



# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleados',
        'USER' : 'hector',
        'PASSWORD' : 'hector01',
        'HOST' : '172.18.0.2',
        'PORT': '5432'

        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR.child('db.sqlite3'),
    }
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
