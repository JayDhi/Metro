# App/User/serializers.py
# import from framework
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
# import from project
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)
    
class RegisterUser(serializers.ModelSerializer):
    role = serializers.CharField(required=False)
    token = serializers.SerializerMethodField()
    def get_token(self, instance):
        tokens = RefreshToken.for_user(instance)
        data={}
        data['refresh'] = str(tokens)
        data['access'] = str(tokens.access_token)
        return data
    def create(self, data):
        user = User.objects.create_user(username=data["username"])
        user.set_password(data["password"])
        user.save()
        return user
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop("password")
        return data
    class Meta:
        model = User
        fields = ('username', 'password', 'role', 'token')
class AdminUser(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    role = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = ('id', 'username', 'role')