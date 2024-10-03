"""
ASGI config for talkytalk project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'talkytalk.settings')

application = get_asgi_application()

# channels 라우팅과 미들웨어는 django 초기화 이후에 가져오기
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
import chatting.routing

application = ProtocolTypeRouter({
    'http': application,
    'websocket': AuthMiddlewareStack(
            AllowedHostsOriginValidator(
            URLRouter(
                chatting.routing.websocket_urlpatterns
            )     
        ),
    ),
})
