# App/User/views.py
# import from framework
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
# import from project
from .models import User
from .serializers import UserSerializer

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def test(request):
    content = {"username": request.user.username, "role": request.user.role, "role_category": request.user.role_category}
    return JsonResponse(content)

@api_view(['GET'])
def user_list(request):
    user_set = User.objects.all()
    user_slzr = UserSerializer(instance=user_set, many=True)
    return JsonResponse(data=user_slzr.data, safe=False)

@api_view(['POST'])
def user_create(request):
    user_slzr = UserSerializer(data=request.data)
    if user_slzr.is_valid():
        user_slzr.save()
        return JsonResponse(data=user_slzr.data, safe=False)
    else:
        return JsonResponse(data=user_slzr.errors)