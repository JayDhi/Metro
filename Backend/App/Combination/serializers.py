# App/Combination/serializers.py
# import from framework
from rest_framework import serializers
import json
# import from project
from .models import RouteXStation

class RouteXStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteXStation
        fields = ('route', 'seq', 'station')