# App/Flow/views.py
# import from framework
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
# import from project
from .models import get_flow_data

@api_view(['GET'])
def show_flow(request):
    data = get_flow_data(year=request.query_params["year"],
                         month=request.query_params["month"],
                         dates=request.query_params["dates"], 
                         stations=request.query_params["stations"])
    return JsonResponse(data=data, safe=False)