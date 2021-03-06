"""
Django settings for Blog project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

#from decouple import config

#import dj_database_url



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#We have moved our settings files to a directory one level lower, so we need BASE_DIR to point to the parent directory to be correct.
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = config('SECRET_KEY')
SECRET_KEY = 'v47!o*60a)#w*)mfqim02k0-x@ilf46b%ssk9!%$6tpe&h=w2i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


#DATABASES = {
#    'default': 'postgres://eqhdbyqwvhzacz:28eafdfb798dfcb6a079547b85dba1b424a49bd2d0dfcb77521215a22d206494@ec2-23-23-101-25.compute-1.amazonaws.com:5432/d3sflal2o13ccj'

#}


ALLOWED_HOSTS = ['.herokuapp.com', '127.0.0.1', '.pythonanywhere.com', 'karenniblog.pythonanywhere.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Post',
    'bootstrap4',
    'taggit',
    'django.contrib.postgres',
    'accounts',
    'social_django',
    'crispy_forms',
    'rest_framework',
    'taggit_serializer',
    'tinymce',
    'filebrowser',



    #'haystack'
    
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



ROOT_URLCONF = 'Blog.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'Blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#

#DATABASES = {
 #   'default': {
  #      'ENGINE': 'django.db.backends.postgresql',
   #   'PASSWORD': 'Pa$$w0rd',
    ## 'PORT':'5432',
    #}
#}


#db_from_env = dj_database_url.config()
#DATABASES['default'].update(db_from_env)
#DATABASES['default']['CONN_MAX_AGE'] = 500

#HAYSTACK_CONNECTIONS = {

#'default': {
#'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
#'URL': 'http://127.0.0.1:8983/solr'
#},

#}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/


STATIC_URL = '/static/'

STATICFILES_DIRS = ( os.path.join(BASE_DIR, 'Post/static'), )


STATIC_ROOT = os.path.join(BASE_DIR, "live-static-files", "static-root")




EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'your_account@gmail.com'
EMAIL_HOST_PASSWORD = 'your_password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'



MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "live-static-files", "media-root")

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}



#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticsFilesStorage'
#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': 1120,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
    }


FILEBROWSER_DIRECTORY = ''
DIRECTORY = ''