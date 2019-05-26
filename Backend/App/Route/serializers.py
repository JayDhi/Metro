# App/Route/serializers.py
# import from framework
from rest_framework import serializers
# import from project
from .models import Route
from App.Combination.serializers import RouteXStationSerializer

class RouteSerializer(serializers.ModelSerializer):
    stations = RouteXStationSerializer(source='routexstation_set', required=False, many=True)
    class Meta:
        model = Route
        fields = ('route_id', 'stations')