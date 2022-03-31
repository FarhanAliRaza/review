
from pathlib import Path
import os
import dj_database_url


BASE_DIR = Path(__file__).resolve().parent.parent

# BASE_URL = "http://127.0.0.1:8000"
BASE_URL = "https://reviewstore2.herokuapp.com"


SECRET_KEY = 'django-insecure-2*(1j(_3ox)%(t3xb73p^^o$m%!l6-&s@v!tszxob-7$o3qsrv'

AUTH_USER_MODEL = 'accounts.User'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com', '*']
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'accounts',
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

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'app.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'myprojectdb',
#         'USER': 'myprojectuser',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TEMPLATE_DIRS = [BASE_DIR / "template"]
# STATIC_ROOT = BASE_DIR / "static"
# STATICFILES_DIRS = [BASE_DIR / "static"]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media_root"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
