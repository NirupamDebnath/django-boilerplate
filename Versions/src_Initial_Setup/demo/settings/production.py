from .base import *

DEBUG = False
ALLOWED_HOSTS = ['ip-address','www.myhost.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "db-name",
        'USER': 'USER-name',
        'PASSWORD': 'db-pass',
        'HOST': 'localhost',
        'PORT': ''
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

STRIPE_PUBLIC_KEY = 'my-live-public-key'
STRIPE_SECRET_KEY = 'my-live-secret-key'