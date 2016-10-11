# -*- coding: utf-8 -*-

"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
from base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*", ]

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'the_thing',
        'USER':'nirlendu',
        'HOST': 'localhost',
    }
}

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings.local'



#VERY IMPORTANT! - This is referred everywhere
GRAPHDB_URL = 'http://localhost:7474/'

REACT = {
    'RENDER': True,
    'RENDER_URL': 'http://127.0.0.1:9009',
}