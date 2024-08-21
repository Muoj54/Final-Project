"""
WSGI config for MatatuFinder project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MatatuFinder.settings')

application = get_wsgi_application()

app = application
"""
# This file contains the WSGI configuration required to run the Django application
from django.core.wsgi import get_wsgi_application

# Get the WSGI application
application = get_wsgi_application()

# Apply WSGI middleware as needed
# For example, to add a custom header to all responses:
def custom_header_app(environ, start_response):
    def custom_header_status(status, headers, exc_info=None):
        start_response(status, headers)
        return iter([])

    d = custom_header_status('200 OK', [('Content-Type', 'text/plain')])
    yield b"Custom header from WSGI middleware\n"
    yield from application(environ, d)

# Wrap the application with the custom header middleware
application = custom_header_app(application)
"""
