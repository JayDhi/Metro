# App/Operation/serializers.py
# import from framework
from rest_framework import serializers
from rest_framework.reverse import reverse
import traceback
# import from project
from .models import Operation

class OperationSerializer(serializers.ModelSerializer):
    sub_operations = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
    def get_url(self, obj):
        if obj.app_name == "" or obj.view_name == "":
            return None
        else:
            return reverse("%s:%s" % (obj.app_name, obj.view_name))
    def get_sub_operations(self, obj):
        try:
            # 要将self.context传入迭代列表, 否则迭代停止
            return [OperationSerializer(i, context=self.context).data 
                    for i in Operation.objects.filter(parent_operation_id=obj.operation_id, 
                                                     role_belong_to__contains=str(self.context["role"]))]
        except:
            traceback.print_exc()
            return None
    def create(self, data):
        data["operation_id"] = Operation.objects.count()
        data["parent_operation_id"] = Operation.objects.filter(name=self.context["parent_operation"]).values('operation_id')[0]["operation_id"]
        print(data)
        return Operation.objects.create(**data)
    # 自定义validate: 传入parent_operation_name, data["parent_operation_name"]
    # 但会引发KeyError: 'parent_operation_name'
    # data --> OrderedDict{} 并不含有parent_operation_name, 可能是在最初的过程中被清洗

    def validate(self, data):
        if self.context["parent_operation"] == "":
            return data
        else:
            try:
                Operation.objects.get(name=self.context["parent_operation"])
                return data
            except:
                raise serializers.ValidationError("Parent Operation DOES NOT exist!!")
    class Meta:
        model = Operation
        fields = ('name', 'url', 'description', 'sub_operations')