# ablog/wsgi.py
"""
WSGI config for ablog project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
import sys

# Add your project directory to the sys.path
path = '/home/kiinshuk/theblog'  # Change to your path
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ablog.settings')

application = get_wsgi_application()