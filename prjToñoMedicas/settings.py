"""
Django settings for prjToñoMedicas project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-1q^#j5298or@073f2zv&d^)_=*oqw^sot7wb^kce5wk$vzqtr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'social_django',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appToñoMedicas.apps.ApptoñomedicasConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'prjToñoMedicas.urls'

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

WSGI_APPLICATION = 'prjToñoMedicas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'd9e8agdjst5ap7',
#        'USER': 'wrjspdnyuriemw',
#        'PASSWORD':'b96728e0f5cd1bd66981e76c77b31ce3b3fa11c0146a21f4cb2162b22b8fea1f',
#        'HOST':'ec2-184-72-248-8.compute-1.amazonaws.com',
#        'PORT':'5432'
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'appMedicas',
        'USER': 'postgres',
        'PASSWORD':'1053840370',
        'HOST':'127.0.0.1',
        'PORT':'5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'static'))
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT =os.path.join(BASE_DIR,"staticfiles")
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
#-----------------------------------------------------------------------------
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

AUTHENTICATION_BACKENDS =(
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL ='dashboard'
#SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'picture', 'name']

#SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
#  'fields': 'id, name, email, age_range'
#}

SOCIAL_AUTH_TWITTER_KEY = 'aTKOmPZk2oKch7g1A3vlylKRN'
SOCIAL_AUTH_TWITTER_SECRET = '1631akeuQozq6ePoHeVjXdOEx6XwVDkKQs5YOBT3JQmY1wNsar'

SOCIAL_AUTH_FACEBOOK_KEY = '406705036399443'
SOCIAL_AUTH_FACEBOOK_SECRET = '784686d36d3d5d76b985d5854baa04fd'