from datetime import timedelta
from pathlib import Path

from decouple import config, Csv

from config.logger import Filter, get_logging

SECRET_KEY = config('SECRET_KEY')

BASE_DIR = Path(__file__).resolve().parent.parent.parent

MODE = config('MODE').lower()

SERVICE_KEY = config(
    'SERVICE_KEY',
    default='django-cqrs',
)

INSTALLED_APPS = [
    # * For Admin disables
    'django.contrib.auth',

    # * Default
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # * Apps
    'apps.core.apps.CoreConfig',
    'apps.item.apps.ItemConfig',

    # * Packages
    'corsheaders',
    'rest_framework',

    # * Healthcheck
    'health_check',
    'health_check.db',
    'health_check.contrib.migrations',
]

MIDDLEWARE = [
    # * Default
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # * Packages
    'corsheaders.middleware.CorsMiddleware',
]

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

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DATETIME_INPUT_FORMAT = DATETIME_FORMAT
DATE_FORMAT = '%Y-%m-%d'

USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ADMIN_USERNAME = config('ADMIN_USERNAME')
ADMIN_PASSWORD = config('ADMIN_PASSWORD')


# * -------------------------------- Logger ---------------------------------
class LoggingFilter(Filter):
    service = SERVICE_KEY


LOGGING = get_logging(filter=LoggingFilter)
# * -------------------------------------------------------------------------

# * ------------------------------- Databases -------------------------------
# * PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_PRIMARY_DB_NAME'),
        'USER': config('POSTGRES_PRIMARY_DB_USER'),
        'PASSWORD': config('POSTGRES_PRIMARY_DB_PASSWORD'),
        'HOST': config('POSTGRES_PRIMARY_DB_HOST'),
        'PORT': config(
            'POSTGRES_PRIMARY_DB_PORT',
            cast=int,
        ),
    },
    'replica': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_REPLICA_DB_NAME'),
        'USER': config('POSTGRES_REPLICA_DB_USER'),
        'PASSWORD': config('POSTGRES_REPLICA_DB_PASSWORD'),
        'HOST': config('POSTGRES_REPLICA_DB_HOST'),
        'PORT': config(
            'POSTGRES_REPLICA_DB_PORT',
            cast=int,
        ),
    }
}
# * -------------------------------------------------------------------------

# * ---------------------------------- API ----------------------------------
ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'
ASGI_APPLICATION = 'config.asgi.application'

ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    cast=Csv(),
)

CORS_ORIGIN_ALLOW_ALL = config(
    'CORS_ORIGIN_ALLOW_ALL',
    cast=bool,
)

CSRF_TRUSTED_ORIGINS = config(
    'CSRF_TRUSTED_ORIGINS',
    cast=Csv(),
)
CSRF_COOKIE_SECURE = config(
    'CSRF_COOKIE_SECURE',
    cast=bool,
)

PAGE_SIZE = config(
    'PAGE_SIZE',
    default=10,
    cast=int,
)

ACCESS_TOKEN_LIFETIME = config(
    'ACCESS_TOKEN_LIFETIME',
    default=1440,
    cast=int,
)
REFRESH_TOKEN_LIFETIME = config(
    'REFRESH_TOKEN_LIFETIME',
    default=16,
    cast=int,
)

SIGNING_KEY = config('SIGNING_KEY')

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(ACCESS_TOKEN_LIFETIME),
    'REFRESH_TOKEN_LIFETIME': timedelta(REFRESH_TOKEN_LIFETIME),
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SIGNING_KEY,
    'USER_ID_CLAIM': 'id',
    'TOKEN_TYPE_CLAIM': 'type',
    'AUTH_HEADER_TYPES': ('jwt', ),
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':
    ('rest_framework_simplejwt.authentication.JWTTokenUserAuthentication', ),
    'DEFAULT_PAGINATION_CLASS':
    'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE':
    PAGE_SIZE,
    'DATETIME_FORMAT':
    DATETIME_FORMAT,
    'DATE_FORMAT':
    DATE_FORMAT,
}
# * -------------------------------------------------------------------------
