import os
import django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lemarche.settings")
print(f'DJANGO_SETTINGS_MODULE: {os.environ.get("DJANGO_SETTINGS_MODULE")}')
django.setup()

import core.routing


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
         "websocket": 
            AuthMiddlewareStack(URLRouter(core.routing.websocket_urlpatterns))
        
    }
)
class CustomMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        await self.app(scope, receive, send)

        # Handle setting headers if needed
        # Example:
        # scope['headers'] = [
        #     (b'Content-Type', b'text/plain'),
        #     (b'Content-Length', b'15'),
        # ]

application = CustomMiddleware(application)

app = application

# import os

# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lemarche.settings')

# application = ProtocolTypeRouter({
#     'http': get_asgi_application(),
# })