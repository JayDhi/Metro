# App/Route/serializers.py
# import from framework
from rest_framework import serializers
# import from project
from .models import Route

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = "__all__"