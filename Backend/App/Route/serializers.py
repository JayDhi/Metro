# App/Route/serializers.py
# import from framework
from rest_framework import serializers
# import from project
from App.Combination.serializers import RouteXStationSerializer
from .models import Route

class RouteSerializer(serializers.ModelSerializer):
    stations = RouteXStationSerializer(source='routexstation_set', required=False, many=True)
    class Meta:
        model = Route
        fields = ('route_id', 'stations')