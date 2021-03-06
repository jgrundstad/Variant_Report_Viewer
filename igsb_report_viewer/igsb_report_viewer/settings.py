from secret_settings import secret_key
"""
Django settings for igsb_report_viewer project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
#ALLOWED_HOSTS = ['128.135.*.*']


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'viewer',
    'django_extensions',
    'django_crontab',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    )

ROOT_URLCONF = 'igsb_report_viewer.urls'

WSGI_APPLICATION = 'igsb_report_viewer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': BASE_DIR + '/igsb_report_viewer/my.cnf',
        },
    }
}

CRONJOBS = [
        #('* * * * *', 
        #    'viewer.links_out.cron.run_cron_test')
        ('10 2 * * *',
            'viewer.links_out.cron.gather_md_anderson')
]

GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Central'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT = BASE_DIR + '/viewer/files/'
MEDIA_URL = '/viewer/files/'
LINKS_OUT = BASE_DIR + '/viewer/links_out/'
LOGIN_URL = '/viewer/login/'

print "BASE_DIR: " + BASE_DIR
print "MEDIA_ROOT: " + MEDIA_ROOT
print "MEDIA_URL: " + MEDIA_URL
print "LINKS_OUT: " + LINKS_OUT