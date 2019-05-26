# App/Station/serializer.py
# import from framework
from rest_framework import serializers
# import from project
from .models import Station
from App.Combination.serializers import RouteXStationSerializer

class StationSerializer(serializers.ModelSerializer):
    station_id = serializers.IntegerField(required=False)
    routes = RouteXStationSerializer(source='routexstation_set', required=False, many=True)
    class Meta:
        model = Station
        fields = "__all__"