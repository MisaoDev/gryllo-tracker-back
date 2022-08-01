"""
ASGI config for gryllo_tracker project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

from gryllo_tracker.util import set_settings_module


set_settings_module(os.getenv('ENV'))

application = get_asgi_application()
