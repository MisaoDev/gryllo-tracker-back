"""
WSGI config for gryllo_tracker project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import socketio
from gevent import pywsgi

from django.core.wsgi import get_wsgi_application

from gryllo_tracker.util import set_settings_module


set_settings_module(os.getenv('ENV'))

from .sio import sio

application = get_wsgi_application()
application = socketio.WSGIApp(sio, application)

PORT = int(os.environ.get('PORT', 8000))
pywsgi.WSGIServer(
    ('', PORT),
    application,
).serve_forever()
