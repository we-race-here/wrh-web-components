from django.contrib import admin
from django.urls import path
from .rest_api import routers, viewsets
urlpatterns = [
]
urlpatterns += routers.zwift_route.urls