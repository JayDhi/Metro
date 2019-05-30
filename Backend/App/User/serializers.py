# App/User/serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)
    
class RegisterUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
class AdminUser(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    role = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = ('id', 'username', 'role')