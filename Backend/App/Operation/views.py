# App/Operation/views.py
# import from framework
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# import from project
from .models import Operation
from .serializers import OperationSerializer

# TO-DO: 用装饰器实现菜单过滤以及角色验证
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_user_menu(request):
    print(request.user.role)
    top_operations = Operation.objects.filter(role_belong_to__contains=str(request.user.role), parent_operation=0)
    menu = OperationSerializer(top_operations, context={"role": str(request.user.role)}, many=True)
    print(menu.data)
    return JsonResponse(data=menu.data, safe=False)

# 添加菜单根节点的时候需要将其parent_operation设为NullOperation # fix: 处理MySQL中Null字段

# 由于数据库设计的缘故需要手动生成operation_id(主键),
# 在有0号对象(NullOperation)的情况下operation_id=Operation.objects.count()
# validate()检测是否存在父节点对象
@api_view(['POST'])
@permission_classes((IsAdminUser,))
# input json format {"parent_operation", "name", }
def add_operation(request):
    serializer = OperationSerializer(data=request.data, context={"parent_operation": request.data["parent_operation"]})
    pass

@api_view(['POST'])
@permission_classes((IsAdminUser,))
def link(request):
    pass