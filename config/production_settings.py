import os
from pathlib import Path
from .settings import *

# Get BASE_DIR from settings or define it
BASE_DIR = Path(__file__).resolve().parent.parent

# Production settings for PythonAnywhere
DEBUG = False

# Replace 'yourusername' with your actual PythonAnywhere username
ALLOWED_HOSTS = ['akbrln.pythonanywhere.com']

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = '/home/akbrln/laporan_magang/static'

# Media files configuration  
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/akbrln/laporan_magang/media'

# Security settings
SECURE_SSL_REDIRECT = False  # Set to True if using HTTPS
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Database - keep SQLite for free tier
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/akbrln/laporan_magang/db.sqlite3',
    }
}