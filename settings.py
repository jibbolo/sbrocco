import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_PATH = os.path.dirname(__file__)

# TWITTER

CONSUMER_KEY = "IaLJ9girzWQxCvXcVPSiA"
CONSUMER_SECRET = "9shWurByIKXG1Yvc5kb0vmBMpavbhMiGmJg9FSgBGJA"

ADMINS = (
    ('Giacomo', 'jibbolo@gmail.com'),
    ('Diego', 'diegor.it@gmail.com'),
    ('Lorenzo', 'l.allegrucci@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': os.path.join(PROJECT_PATH,'sbrocco.db'),  
        'USER': '',                             
        'PASSWORD': '',                         
        'HOST': '',                             
        'PORT': '',                
    }
}

TIME_ZONE = 'Europe/Rome'

LANGUAGE_CODE = 'en'

SITE_ID = 1
USE_I18N = True
USE_L10N = True
MEDIA_ROOT = ''
MEDIA_URL = ''
ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = '3ilk$c)*&b5ry=ygbs(&as9*dh&tm#6b!q010w&!d++z!du294'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'sbrocco.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH,"templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'sbrocco.account',
    # 'django.contrib.admin',
)
