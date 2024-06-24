"""
Django settings for share project.

Generated by 'django-admin startproject' using Django 4.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from pathlib import Path
import os
import configparser
from web3 import Web3

from django.utils.translation import gettext_lazy as _

from google.oauth2 import service_account
import google.auth
from google.auth import load_credentials_from_file


from dotenv import load_dotenv

load_dotenv()
"""
config=configparser.ConfigParser()
path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
config.read(os.path.join(path, 'config.ini'))

google_maps_api_key = config['credentials']['google_maps_api_key']
email_host_password = config['credentials']['email_host_password']
database_password = config['credentials']['database_password']
private_key = config['credentials']['private_key']
"""

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i9v3x)_xkl2ptnh=k2nk!0tm%xu5j&&&yqz#+l4^xenm0*za(3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
PRODUCTION = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'contribute',
    'borrow',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'share.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'borrow.views.airdrop_amount_processor',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'share.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
LANGUAGES = [
    ('en', 'English'),
    ('zh-hant', 'Traditional Chinese'),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True  
USE_L10N = True
USE_TZ = True 


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
 

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'login'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'sharetoearn999@gmail.com'
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')

PRIVATE_KEY = os.getenv('PRIVATE_KEY')


if PRODUCTION:
    
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/secrets/key.json'

    # Now load the credentials
    try:
        credentials, project_id = load_credentials_from_file(os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))
    except Exception as e:
        print(f"Error loading Google credentials: {e}")
        
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'ntub_project_share_db',
            'USER': 'jimwu',
            'PASSWORD': os.getenv('GCP_DATABASE_PASSWORD'),
            #'HOST': '/cloudsql/ntub-senior-project-427211:asia-east1:ntub-senior-project-instance', 
            'HOST' : '127.0.0.1',
            'PORT': '5432',
        }
    }
  
    DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    GS_BUCKET_NAME = 'ntub-share-to-earn-bucket'

    STATIC_URL = f'https://storage.googleapis.com/{GS_BUCKET_NAME}/static/'
    MEDIA_URL = f'https://storage.googleapis.com/{GS_BUCKET_NAME}/media/'
    
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]

else:
    
    if DEBUG:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'ntub_project_share_db',
                'USER': 'postgres',
                'PASSWORD': os.getenv('DATABASE_PASSWORD'),
                'HOST': 'localhost',
                'PORT': '5432'
            }
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'ntub_project_share_db',
                'USER': 'postgres',
                'PASSWORD': os.getenv('DATABASE_PASSWORD'),
                'HOST': os.getenv('DB_HOST'),
                'PORT': '5432'
            }
        }
        
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



