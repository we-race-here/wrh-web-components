from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, mixins
from rest_framework.viewsets import GenericViewSet

from apps.zwift_components import models
from . import serializers, customfilters
import requests



class TeamResultViewset(
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = serializers.TeamResultSerailizersTeamResultSerailizers
    queryset = models.TeamResult.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = customfilters.FilterFilter

    def list(self, request, *args, **kwargs):
        """
        Team Result API
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        res = super().list(request, *args, **kwargs)
        if request.GET.get('tid') and models.TeamResult.objects.filter(tid=request.GET.get('tid')).count() == 0:
            # Fetching data from https://zwiftapi.weracehere.org
            urls = f"https://zwiftapi.weracehere.org/team_results?id={request.GET.get('tid')}"
            z_wrh = requests.get(urls)
            if z_wrh.status_code == 200:
                seralizer = serializers.TeamResultSerailizersTeamResultSerailizers(data=z_wrh.json().get('data'), many=True)
                seralizer.is_valid(raise_exception=True)
                seralizer.save()
                res = super().list(request, *args, **kwargs)
        return res


