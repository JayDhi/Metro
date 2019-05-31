# App/Station/views.py
# import from framework
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
# import from project
from .models import Station
from .serializers import ShowStation, EditStation

@api_view(['GET'])
def get_station(request):
    if "station" in request.data:
        slzr = ShowStation(Station.objects.filter(
                                        station_id__in=request.data["station"]), 
                                            many=True)
    else:
        slzr = ShowStation(Station.objects.all(), many=True)
    return JsonResponse(data=slzr.data, safe=False)
    

# input format
# {"station": {"station_name"}, "relation": {"route"}}
# validate customize: relation
@api_view(['POST'])
def edit_station(request):
    data = request.data["station_info"]
    context = request.data["relationship"]
    try:
        station = Station.objects.get(station_name=data["station_name"])
    except KeyError:
        return JsonResponse(data={"errors": "Check Json Parameter"})
    except Station.DoesNotExist:
        slzr = EditStation(data=data, context=context)
    else:
        slzr = EditStation(station, data=data, context=context)
    if slzr.is_valid():
        slzr.save()
        return JsonResponse(data=slzr.data, safe=False)
    else:
        return JsonResponse(slzr.errors)
    