# App/Flow/views.py
# import from framework
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
# import from project
from .models import get_flow_data

@api_view(['GET'])
def show_flow(request):
    data = get_flow_data(request.data["dates"], request.data["stations"])
    return JsonResponse(data=data, safe=False)