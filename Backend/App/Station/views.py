# App/Station/views.py
# import from framework
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
# import from project
from .models import Station
from .serializers import StationSerializer

@api_view(['GET'])
def station_list(request):
    station_set = Station.objects.all()
    station_slzr = StationSerializer(instance=station_set, many=True)
    return JsonResponse(data=station_slzr.data, safe=False)

@api_view(['POST'])
def station_create(request):
    station_slzr = StationSerializer(data=request.data)
    if station_slzr.is_valid():
        station_slzr.save()
        return JsonResponse(data=station_slzr.data, safe=False)
    else:
        return JsonResponse(station_slzr.errors)