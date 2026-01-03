import os
import sys

# Add your project directory to Python path
path = '/home/akbrln/laporan_magang'  # Replace 'yourusername' with your PythonAnywhere username
if path not in sys.path:
    sys.path.insert(0, path)

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.production_settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()