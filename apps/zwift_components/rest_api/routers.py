from rest_framework import routers
from . import viewsets
zwift_route = routers.DefaultRouter()

zwift_route.register('teamresult', viewsets.TeamResultViewset)