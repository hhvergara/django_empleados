from .base import *
from empleados.settings import init

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

        # Base de datos Postgres de docker en ubuntu:
        # Docker pull:
        # docker pull hhvergara/postgres_adminer_1
        # docker pull hhvergara/postgres_db_1

        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleados',
        'USER' : 'hector',
        'PASSWORD' : 'hector01',
        'HOST':'localhost',
        'PORT': '5432'

        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR.child('db.sqlite3'),
    }
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
