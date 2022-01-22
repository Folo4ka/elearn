from .base import *

DEBUG = False
ADMINS = (
    ('admin', 'admin@admin.com'),
)
ALLOWED_HOSTS = ['.elearnproject.com']

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'elearn',
       'USER': 'ivan',
       'PASSWORD': '******',
   }
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True

