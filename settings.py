import socket
import os
import django
# calculated paths for django and the site
# used as starting points for various other paths
DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

# Django settings for styleloving project.

if socket.gethostname() == 'server_hostname':
    DEBUG = False
else:
    DEBUG = True
TEMPLATE_DEBUG = DEBUG

INTERNAL_IPS = ('127.0.0.1',)

ADMINS = (
    ('Author', 'email@myproject.com'),
)

MANAGERS = ADMINS

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'dev.db',                      # Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'myproject',                      # Or path to database file if using sqlite3.
            'USER': 'myproject',                      # Not used with sqlite3.
            'PASSWORD': 'myproject_passwd',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
if DEBUG:
    MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')
else:
    MEDIA_ROOT = os.path.join(SITE_ROOT, '../media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'e=(=3bmff#vv12X/_zl-123d55&7((<<12h@ghuevy)#e5i1^1z@wz=+i340%diz'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)

if DEBUG:
    MIDDLEWARE_CLASSES = (
        'annoying.middlewares.StaticServe',
        #'debug_toolbar.middleware.DebugToolbarMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    )
else:
    MIDDLEWARE_CLASSES = (
        #'johnny.middleware.LocalStoreClearMiddleware',
        #'johnny.middleware.QueryCacheMiddleware',
        'annoying.middlewares.StaticServe',
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    )

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'myproject.urls'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'django.contrib.flatpages',
    #'django.contrib.sitemaps',
    
    # 3rd party apps
    'annoying',
    'south',
    'robots',
    'debug_toolbar',
    'compressor',
    #'postmark',
    #'johnny', # Johnny Cache
    
    # Project apps
    'main',
)

if not DEBUG:
    INSTALLED_APPS += (
        # Add production apps here (like Johnny Cache)
        #'johnny',
    )

# User Profile
AUTH_PROFILE_MODULE = 'main.UserProfile'

# URLs
LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Email servers
if DEBUG:
    # Print to console
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    # Uncomment the following line to user django-postmark for sending email (install with pip first)
    #EMAIL_BACKEND = 'postmark.django_backend.EmailBackend'
    
    # Postmark settings
    POSTMARK_API_KEY    = ''
    POSTMARK_SENDER     = 'hello@domain.com'
    DEFAULT_FROM_EMAIL  = 'hello@domain.com' # django-notification
    SERVER_EMAIL        = 'hello@domain.com' # django errors
    SEND_BROKEN_LINK_EMAILS = True # Email about 404s at start
    


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

# CSS compiler setup
COMPILER_FORMATS = {
    '.ccss': {
        'python':'clevercss.convert',
        'arguments': '*.ccss',
    },
}
COMPRESS = True
