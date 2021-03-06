# -*- coding: utf8 -*-

u"""
    Mathics: a general-purpose computer algebra system
    Copyright (C) 2011-2013 The Mathics Team

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import pkg_resources
import sys
import os
from os import path

import django
import dj_database_url
DJANGO_VERSION = django.VERSION

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# set only to True in DEBUG mode
DEBUG_MAIL = True
PROPAGATE_EXCEPTIONS = True
DISPLAY_EXCEPTIONS = True
DEBUG_PRINT = False

LOG_QUERIES = False

TIMEOUT = None
MAX_RECURSION_DEPTH = 512

# number of bits of precision for inexact calculations
MACHINE_PRECISION = 64

ADMINS = (
    (u'Admin', 'mail@test.com'),
)
MANAGERS = ADMINS

ROOT_DIR = pkg_resources.resource_filename('mathics', '') + '/'
if sys.platform.startswith('win'):
    DATA_DIR = os.environ['APPDATA'].replace(os.sep, '/') + '/Python/Mathics/'
else:
    DATA_DIR = path.expanduser('~/.local/var/mathics/')
# if not path.exists(DATA_DIR):
#    os.makedirs(DATA_DIR)

DOC_DIR = ROOT_DIR + 'doc/documentation/'
DOC_TEX_DATA = ROOT_DIR + 'doc/tex/data'
DOC_XML_DATA = ROOT_DIR + 'doc/xml/data'
DOC_LATEX_FILE = ROOT_DIR + 'doc/tex/documentation.tex'

DATABASES = {
    'default': dj_database_url.config()
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

REQUIRE_LOGIN = True

SERVER_EMAIL = 'mathics@localhost'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Vienna'

# Set this True if you prefer 12 hour time to be the default
TIME_12HOUR = False

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# Leave this True unless you have specific reason for not permitting
# users to access local files
ENABLE_FILES_MODULE = True

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ROOT_DIR + 'web/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/media/", "/media/".
if DJANGO_VERSION < (1, 3):
    ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'uvbhuiasaeaph6Duh)r@3ex1i@et=0j4h(!p4@!r6s-=a_ev*e'

# List of callables that know how to import templates from various sources.
# TEMPLATE_LOADERS = (
#    'django.template.loaders.filesystem.load_template_source',
#    'django.template.loaders.app_directories.load_template_source',
#)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'mathics.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or
    # "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    ROOT_DIR + 'web/templates/',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
)

AUTHENTICATION_BACKENDS = (
    'mathics.web.authentication.EmailModelBackend',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.messages',
    'mathics.web',
)
