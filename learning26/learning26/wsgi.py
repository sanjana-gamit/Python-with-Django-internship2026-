"""
WSGI config for learning26 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import sys

try:
    from django.core.wsgi import get_wsgi_application  # type: ignore
except ImportError as e:
    print(f"Error: Django is not installed. Please install it using: pip install django")
    sys.exit(1)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning26.settings')

application = get_wsgi_application()
