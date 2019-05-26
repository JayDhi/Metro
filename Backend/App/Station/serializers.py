# App/Station/serializer.py
# import from framework
from rest_framework import serializers
# import from project
from .models import Station

class StationSerializer(serializers.ModelSerializer):
    station_id = serializers.IntegerField(required=False)
    class Meta:
        model = Station
        fields = "__all__"