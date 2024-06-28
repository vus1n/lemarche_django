from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path("ws/chat/<str:user1>/<str:user2>/<str:room_name>/", consumers.ChatConsumer.as_asgi()),
]