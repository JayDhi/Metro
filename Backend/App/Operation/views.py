# App/Operation/views.py
# import from framework
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# import from project
from .models import Operation
from .serializers import ShowOperation, EditOperation

# -[x] Create
# -[x] Retrive
# -[x] Update
# -[ ] Delete

# TO-DO: 用装饰器实现菜单过滤以及角色验证
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_menu(request):
    # 不用get()而用filter()
    top_operations = Operation.objects.filter(role__contains=str(request.user.role), parent_operation=0)
    menu = ShowOperation(top_operations, context={"role": str(request.user.role)}, many=True)
    return JsonResponse(data=menu.data, safe=False)

# 添加菜单根节点的时候需要将其parent_operation设为NullOperation # fix: 处理MySQL中Null字段

# 由于数据库设计的缘故需要手动生成operation_id(主键),
# 在有0号对象(NullOperation)的情况下operation_id=Operation.objects.count()
# validate()检测是否存在父节点对象

# 修改菜单栏: 重链父子节点、修改角色过滤
# 需要管理员权限
@api_view(['POST'])
def edit_menu(request):
    try:
        operation = Operation.objects.get(operation_id=request.data["operation_id"])
    except:
        slzr = EditOperation(data=request.data)
    else:
        slzr = EditOperation(instance=operation, data=request.data)
    if slzr.is_valid():
        slzr.save()
        return JsonResponse(data=slzr.data, safe=False)
    else:
        return JsonResponse(slzr.errors)