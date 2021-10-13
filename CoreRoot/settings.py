#! /usr/bin/env python
"""
------------------------------------------------------------------------------------------------------------------------
                  ____        __  __                   __  __               __
                 / __ \__  __/ /_/ /_  ____  ____     / / / /__  ____ _____/ /__  _____
 ____________   / /_/ / / / / __/ __ \/ __ \/ __ \   / /_/ / _ \/ __ `/ __  / _ \/ ___/  ____________
/_____/_____/  / ____/ /_/ / /_/ / / / /_/ / / / /  / __  /  __/ /_/ / /_/ /  __/ /     /_____/_____/
              /_/    \__, /\__/_/ /_/\____/_/ /_/  /_/ /_/\___/\__,_/\__,_/\___/_/
                    /____/
------------------------------------------------------------------------------------------------------------------------
:FILE:      DjangoBackend-ReactFrontend/CoreRoot/settings.py
:AUTHOR:    Nathan E White, PhD
:ABOUT:     Sets a variety of project and site settings consumed throughout the Django project
------------------------------------------------------------------------------------------------------------------------
:NOTES:     For more information on this file, see:
                            https://docs.djangoproject.com/en/3.1/topics/settings/

            For a full list of settings in Django applications:
                            https://docs.djangoproject.com/en/3.1/ref/settings/

            For a list of 'quick 'n' dirty' settings suitable for dev but not production:
                            https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/
------------------------------------------------------------------------------------------------------------------------
"""
# <BOF>


#   Imports --- Python STL Imports: For manipulating filesystem paths
from pathlib import Path

#   Imports --- Python STL Imports: For importing environmental variables
# noinspection PyUnresolvedReferences
import os


# ----------------------------------------------------------------------------------------------------------------------
#   Application definitions


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# TODO: NEVER LEAVE THIS IN PRODUCTION CODE -- PUT IT IN AN ENVIRONMENTAL VARIABLE
# SECRET_KEY = os.getenv(key = 'DJANGO_KEY')
SECRET_KEY = 'qkl+xdr8aimpf-&x(mi7)dwt^-q77aji#j*d#02-5usa32r9!y'

# TODO: NEVER SET TO TRUE IN A LIVE WEBSITE -- YOU WILL BE HACKED PRONTO
# noinspection DjangoDebugModeSettings
DEBUG = True

ALLOWED_HOSTS = []

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'core',
    'core.user'
    ]

AUTH_USER_MODEL = 'core_user.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

ROOT_URLCONF = 'CoreRoot.urls'

# ----------------------------------------------------------------------------------------------------------------------
#   Templates
#   https://docs.djangoproject.com/en/3.2/topics/templates/

TEMPLATES = [
    {
        'BACKEND':  'django.template.backends.django.DjangoTemplates',
        'DIRS':     [],
        'APP_DIRS': True,
        'OPTIONS':  {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

# ----------------------------------------------------------------------------------------------------------------------
#   WSGI: (Python) Web Service Gateway Interface
#   https://wsgi.readthedocs.io/en/latest/
#   https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/

WSGI_APPLICATION = 'CoreRoot.wsgi.application'

# ----------------------------------------------------------------------------------------------------------------------
#   Database Settings
#   https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':   BASE_DIR / 'db.sqlite3',
        }
    }

# ----------------------------------------------------------------------------------------------------------------------
#   Password validation
#   https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

# ----------------------------------------------------------------------------------------------------------------------
#   Internationalization
#   https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ----------------------------------------------------------------------------------------------------------------------
#   Static files (CSS, JavaScript, Images)
#   https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# ----------------------------------------------------------------------------------------------------------------------
#   REST Framework Definitions
#   https://www.django-rest-framework.org/

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        ),
    'DEFAULT_RENDERER_CLASSES':       (
        'rest_framework.renderers.JSONRenderer',
        )
    }

# ----------------------------------------------------------------------------------------------------------------------
#   CORS Headers
#   https://www.stackhawk.com/blog/django-cors-guide/

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    ]

# ----------------------------------------------------------------------------------------------------------------------
# <EOF>
