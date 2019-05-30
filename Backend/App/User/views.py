# App/User/views.py
# import from framework
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
# import from project
from .models import User
from .serializers import UserSerializer, AdminUser, RegisterUser

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def test(request):
    content = {"username": request.user.username, "role": request.user.role, "role_category": request.user.role_category}
    return JsonResponse(content)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def view_profile(request):
    user = User.objects.get(id=request.user.id)
    user_slzr = UserSerializer(instance=user)
    return JsonResponse(data=user_slzr.data)

# !Admin Required #
@api_view(['GET', 'POST'])
def admin_user(request):
    if request.method == 'GET':
        user_set = User.objects.all()
        user_slzr = AdminUser(instance=user_set, many=True)
        return JsonResponse(data=user_slzr.data, safe=False)
    else:
        try:
            
            user = User.objects.get(id=request.data["id"])
            print(request.data["id"])
            user_slzr = AdminUser(instance=user, data=request.data)
        except:
            return JsonResponse(data={'error': 'User DOES NOT exist'})
        if user_slzr.is_valid():
            user_slzr.save()
            return JsonResponse(data=user_slzr.data, safe=False)
        else:
            return JsonResponse(data=user_slzr.errors, safe=False)
        

# register
@api_view(['POST'])
def register(request):
    user_slzr = RegisterUser(data=request.data)
    if user_slzr.is_valid():
        user_slzr.save()
        return JsonResponse(data=user_slzr.data, safe=False)
    else:
        return JsonResponse(data=user_slzr.errors)