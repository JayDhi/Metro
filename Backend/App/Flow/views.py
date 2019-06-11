# App/Flow/views.py
# import from framework
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
# import from project
from .models import get_flow_data

@api_view(['GET'])
def show_flow(request):
    # print(request.GET['year'])
    print(request.GET)
    data = get_flow_data(year=request.GET["year"],
                         month=request.GET["month"],
                         dates=request.GET["dates"], 
                         stations=request.GET["stations"])
    return JsonResponse(data=data, safe=False)