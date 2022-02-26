from apps.zwift_components import models
from rest_framework import serializers


class TeamResultSerailizersTeamResultSerailizers(serializers.ModelSerializer):
    class Meta:
        model = models.TeamResult
        fields = '__all__'
