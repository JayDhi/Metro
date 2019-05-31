# App/User/serializers.py
# import from framework
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
# import from project
from .models import User
from App.Operation.models import Operation
from App.Operation.serializers import ShowOperation

# 用于显示个人信息
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

# 用于注册用户
# 唯一在用户数据中插入菜单数据的地方    
class RegisterUser(serializers.ModelSerializer):
    role = serializers.CharField(required=False)
    token = serializers.SerializerMethodField()
    menu = serializers.SerializerMethodField()
    def get_token(self, instance):
        tokens = RefreshToken.for_user(instance)
        data={}
        data['refresh'] = str(tokens)
        data['access'] = str(tokens.access_token)
        return data
    def get_menu(self, instance):
        menu_roots = Operation.objects.filter(parent_operation_id=0, role__contains=str(self.instance.role))
        menu = ShowOperation(menu_roots, many=True, context={"role": self.instance.role})
        return menu.data
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
        fields = ('username', 'password', 'role', 'token', 'menu')

# 用于"管理用户"
class AdminUser(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    role = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = ('id', 'username', 'role')