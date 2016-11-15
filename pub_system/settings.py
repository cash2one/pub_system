# -*- coding:utf-8 -*-

"""
Django settings for pub_system project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jjntl07m(cz5=0^ei^!+g48p=n56$!-p@h8go^%qw28&p99!)h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cmdb',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
  #  'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'pub_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pub_system.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pubsys',
        'HOST': '',
        'PORT':3306,
        'USER':'root',
        'PASSWORD': 'xxxxx'
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    "%s/%s" %(BASE_DIR, "static"),
)

LOGIN_URL = '/login'


# WEBSOCKET_FACTORY_CLASS = 'dwebsocket.backends.uwsgi.factory.uWsgiWebSocketFactory'

LOGGING_stamdard_format = '[%(asctime)s][task_id:%(name)s][%(filename)s:%(lineno)d] [%(levelname)s]- %(message)s'
LOGGING_simple_format = '[%(filename)s:%(lineno)d][%(levelname)s] %(message)s'
LOGGING_request_format = '[%(asctime)s][%(status_code)s][%(request)s] %(message)s'
REST_SESSION_LOGIN = False
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,# this fixes the problem
    'formatters': {
        'standard': {#详细
            'format': LOGGING_stamdard_format
        },
        'simple': {#简单
            'format': LOGGING_simple_format
        },
        'request': {#简单
            'format': LOGGING_request_format
        },
    },
    'filters': {},
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'console':{
            'level': 'INFO',
            'class': 'logging.StreamHandler',#打印到前台
            'formatter': 'simple'
        },
        'default': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR+'/logs/','all.log'), #或者直接写路径：'c:\logs\all.log',
            'maxBytes': 1024*1024*10, # 10 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'request': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR+'/logs/','request.log'), #或者直接写路径：'c:\logs\all.log',
            'maxBytes': 1024*1024*10, # 10 MB
            'backupCount': 5,
            'formatter':'request',
        },
        'db': {
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR+'/logs/','db.log'), #或者直接写路径：'c:\logs\all.log',
            'maxBytes': 1024*1024*10, # 10 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'scprits_handler': {
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR+'/logs/','scprits.log'), #或者直接写路径：'c:\logs\all.log',
            'maxBytes': 1024*1024*10, # 10 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'core': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR+'/logs/','core.log'), #或者直接写路径：'c:\logs\all.log',
            'maxBytes': 1024*1024*10, # 10 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'web_apps': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR+'/logs/','web_apps.log'), #或者直接写路径：'c:\logs\all.log',
            'maxBytes': 1024*1024*10, # 10 MB
            'backupCount': 5,
            'formatter':'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['default','console'],
            'propagate': False,
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['request','default'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'scripts': { # 脚本专用日志
            'handlers': ['scprits_handler','default','console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'web_apps': { # 脚本专用日志
            'handlers': ['web_apps','default'],
            'level': 'DEBUG',
            'propagate': False
        },
        'core': { # 脚本专用日志
            'handlers': ['core','default','console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django.db.backends':{
            'handlers': ['db'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}
