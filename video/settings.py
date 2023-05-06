"""
Django settings for video project.
Generated by 'django-admin startproject' using Django 3.0.
For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=vtbwz)^5ezb+ix4+6901-)rtbm4*2z7(cuiiqtp-j(_4(rt1q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
AUTH_USER_MODEL = 'users.MyUser'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'first',
    'users',
    'rest_framework',
    'rest_framework.authtoken',
    # 'embed_video',
    'crispy_forms',
    'crispy_bootstrap5',
    'coustomadmin',

]

SITE_ID = 1
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'video.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'video.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100
}
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
    # 'ENGINE': 'django.db.backends.mysql',
    # 'NAME': 'videocam',
    # 'USER': 'root',
    #     'PASSWORD': '',
    #     'HOST': 'localhost',
    #     'PORT': '3306',

    # },'OPTIONS': {'init_command': 'SET default_storage_engine=INNODB', },
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# REST_FRAMEWORK = {
# 'DEFAULT_AUTHENTICATION_CLASSES':(
#     'rest_framework_simplejwt.authentication.JWTAuthentication',
#     'rest_framework.authentication.BasicAuthentication',
#     'rest_framework.authentication.SessionAuthentication',

# ),


# 'DEFAULT_PERMISSION_CLASSES':(
#     'rest_framework.permissions.IsAuthenticated',
# )
# }
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'python.sartia@gmail.com'
EMAIL_HOST_PASSWORD = 'pgmmignlqptmblko'


# kaifgit persionaltoken
# git_token=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
# git_new_token=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

# pk
# git token =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

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
