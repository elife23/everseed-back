"""
WSGI config for everseed project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import socketio

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
from backend.views import sio

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'everseed.settings')

backend_app  = StaticFilesHandler(get_wsgi_application())
application = socketio.Middleware(sio, wsgi_app=backend_app, socketio_path='socket.io')
#application = get_wsgi_application()

import eventlet
import eventlet.wsgi

eventlet.wsgi.server(eventlet.listen(('', 8000)), application)