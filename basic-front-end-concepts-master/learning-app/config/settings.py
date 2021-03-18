"""
Django settings for config project.
"""

import os
from corsheaders.defaults import default_headers

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5i%ul!b#rui^zipl!+u5nh0+7@j4wtu6o=!0_99t3axph$@oc='

# SECURITY WARNING: don't run with debug turned on in production!
_debug = os.getenv("DEBUG", 'True')
DEBUG = True if _debug == 'True' or _debug is True else False

ALLOWED_HOSTS = ['*']

APPEND_SLASH = False

# Application definition
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'corsheaders',
    'drf_yasg',
    'rest_framework',

    'course.apps.CourseConfig',
    'student.apps.StudentConfig',
    'enrollment.apps.EnrollmentConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates/'],
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

CORS_ALLOW_HEADERS = default_headers

WSGI_APPLICATION = 'config.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Rest Framework
ENABLE_AUTH = os.getenv("ENABLE_AUTH", 'False')
if ENABLE_AUTH == 'TRUE':
    REST_FRAMEWORK = {
        'EXCEPTION_HANDLER': 'config.custom_exception_handler.custom_exception_handler',
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'authentication.keeps_authentication.KeepsAuthentication'
        ],
        'DEFAULT_PAGINATION_CLASS': 'config.pagination_config.StandardResultsSetPagination',
        'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
        'PAGE_SIZE': 100
    }
else:
    REST_FRAMEWORK = {
        'EXCEPTION_HANDLER': 'config.custom_exception_handler.custom_exception_handler',
        'DEFAULT_PAGINATION_CLASS': 'config.pagination_config.StandardResultsSetPagination',
        'PAGE_SIZE': 100
    }


# SWAGGER
SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,

    'SECURITY_DEFINITIONS': {},

    'VALIDATOR_URL': '',
    'OPERATIONS_SORTER': 'method',
    'TAGS_SORTER': None,
    'DOC_EXPANSION': "list",
    'DEEP_LINKING': False,
    'SHOW_EXTENSIONS': True,

    'DEFAULT_AUTO_SCHEMA_CLASS': 'config.docs.SwaggerAutoSchemaCustom',
    'DEFAULT_MODEL_RENDERING': 'model',
    'DEFAULT_MODEL_DEPTH': 2,
}

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)

CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = (
    'http://localhost:4200',
    'http://127.0.0.1:4200',
    'http://localhost:4100',
    'http://127.0.0.1:4100',
)


# Keycloak Configurations

KEYCLOAK_PUBLIC_KEY = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtmbT6XgN9buXZMF6EAjHRNmfGaarVUbik+KtON1YBp0KgTdJn0lCtxhCq5DtvFLOOBrDccw6/RDjeSWlGEcgqggwjPnDIgdtAtgP83mofiILj0mQZfap3o/WknpR6LlveEeM09jnszCTy+WKGZ+HkOJRnhOo/JR7cKSmQxKjEI6NCCNzC4CkwUrPnE5nBhLDk5MvU9KLsBy1TyXoi7c5sh66SLJwD5yn2EzsIxxxje4fYOsXEf6PD6vsAHvjNQNlFELapQTomCECkAwg0fsDZlGAbyK+FoXt/jquKFZ/rcutoXu5tVVNNSfvs5Q4W931KAzqLozd/grR9HlSZAvVWwIDAQAB"

KEYCLOAK_FORMAT_PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
{}
-----END PUBLIC KEY-----"""

KEYCLOAK_SERVER_URL = os.environ.get("KEYCLOAK_SERVER_URL", "https://iam.keepsdev.com/auth/")
KEYCLOAK_REALM = os.environ.get("KEYCLOAK_REALM", "keeps-dev")
KEYCLOAK_CLIENT_ID = os.environ.get("KEYCLOAK_CLIENT_ID", "konquest")
KEYCLOAK_CLIENT_SECRET_KEY = os.environ.get("KEYCLOAK_CLIENT_SECRET_KEY", '6128ac38-3fcf-4712-81e9-8e307d9bd849')
KEYCLOAK_CLIENT_PUBLIC_KEY = os.environ.get("KEYCLOAK_CLIENT_PUBLIC_KEY", KEYCLOAK_PUBLIC_KEY)

KEYCLOAK_CONFIG = {
    'KEYCLOAK_SERVER_URL': KEYCLOAK_SERVER_URL,
    'KEYCLOAK_REALM': KEYCLOAK_REALM,
    'KEYCLOAK_CLIENT_ID': KEYCLOAK_CLIENT_ID,
    'KEYCLOAK_CLIENT_SECRET_KEY': KEYCLOAK_CLIENT_SECRET_KEY,
    'KEYCLOAK_CLIENT_PUBLIC_KEY': KEYCLOAK_FORMAT_PUBLIC_KEY.format(KEYCLOAK_CLIENT_PUBLIC_KEY),
}


