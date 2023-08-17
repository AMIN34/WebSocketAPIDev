from django.urls import path
from .consumers import SensorDataConsumer

websocket_urlpatterns = [
    path("ws/", SensorDataConsumer.as_asgi()),
]