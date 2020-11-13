"""
Django settings for manejador_estadisticas project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#%ac%asfm!*xwnr9e7g9x(z03km2$8o6nmmv9nke@wnj8j)@j&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['172.24.41.73,', '*', ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'manejador_usuarios',
    'manejador_contenido',
    'manejador_busquedas',
    'universidades',
    'booklick',
    'social_django',

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

ROOT_URLCONF = 'manejador_estadisticas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'manejador_estadisticas', 'templates')],
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

WSGI_APPLICATION = 'manejador_estadisticas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'estadisticasDB',
        'USER': 'DISCigners',
        'PASSWORD': 'DISCigners2020',
        'HOST': 'estadisticas-db.cswghco9spvg.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    },
    # 'estadisticas': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'estadisticas_db',
    #     'USER': 'admin',
    #     'PASSWORD': 'DISCigners2020',
    #     'HOST': 'localhost',
    #     'PORT': '',
    # },
    # 'usuarios': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'usuarios_db',
    #     'USER': 'admin',
    #     'PASSWORD': 'DISCigners2020',
    #     'HOST': 'localhost',
    #     'PORT': '',
    # },
    # 'busquedas': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'busquedas_db',
    #     'USER': 'admin',
    #     'PASSWORD': 'DISCigners2020',
    #     'HOST': 'localhost',
    #     'PORT': '',
    # },
    # 'contenido': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'contenido_db',
    #     'USER': 'admin',
    #     'PASSWORD': 'DISCigners2020',
    #     'HOST': 'localhost',
    #     'PORT': '',
    # }
}

# DATABASE_ROUTERS = ['.db_routers.estadisticas_router.EstadisticasRouter', '.db_routers.usuarios_router.UsuariosRouter',
#                     '.db_routers.busquedas_router.BusquedasRouter', '.db_routers.contenido_router.ContenidoRouter']

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

LOGIN_URL = "/login/auth0"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "http://isis2503-leovap.us.auth0.com/v2/logout?returnTo=http%3A%2F%2F18.206.212.143:8000"
SOCIAL_AUTH_TRAILING_SLASH = False  # Remove end slash from routes

SOCIAL_AUTH_AUTH0_DOMAIN = 'isis2503-leovap.us.auth0.com'
SOCIAL_AUTH_AUTH0_KEY = 'CHXN1UG4xJ1FyKOCn6QgOs8bs9HEFgnn'
SOCIAL_AUTH_AUTH0_SECRET = 'Vkong8k0sKcbGrilIdne5S1bEF2_SWMuKjmnqVTNFaoOmg21IjeCUS-BCSgVoLSk'

SOCIAL_AUTH_AUTH0_SCOPE = ['openid',
                           'profile'
                           ]
AUTHENTICATION_BACKENDS = {'manejador_estadisticas.auth0backend.Auth0', 'django.contrib.auth.backends.ModelBackend',
                           }
