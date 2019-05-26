# App/Route/views.py
# import from framework
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
# import from project
from .models import Route
from .serializers import RouteSerializer

@api_view(['GET'])
def route_list(request):
    route_set = Route.objects.all()
    route_slzr = RouteSerializer(instance=route_set, many=True)
    return JsonResponse(data=route_slzr.data, safe=False)

@api_view(['POST'])
def route_create(request):
    route_slzr = RouteSerializer(data=request.data)
    if route_slzr.is_valid():
        route_slzr.save()
        return JsonResponse(route_slzr.data, safe=False)
    else:
        return JsonResponse(route_slzr.errors)