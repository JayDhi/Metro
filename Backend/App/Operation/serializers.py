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
        # data["parent_operation_id"] = self.get_operation_id(self.context["parent_operation"])
        print(data)
        return Operation.objects.create(**data)
    """def update(self, instance, data):
        # for v in dict(data.items()+self.context.items()):
        # for v in {**data, **self.context}:
        print(dict((k, v) for d in (data, self.context) for k, v in d.items()))
        for k, v in dict((k, v) for d in (data, self.context) for k, v in d.items()).items():
            # print(k, v)
            setattr(instance, k, v)
        instance.save()
        return instance"""
        
    # 自定义validate: 传入parent_operation_name, data["parent_operation_name"]
    # 但会引发KeyError: 'parent_operation_name'
    # data --> OrderedDict{} 并不含有parent_operation_name, 可能是在最初的过程中被清洗

    def validate(self, data):
        if 'parent_operation' in self.context:
            try:
                data["parent_operation_id"] = Operation.objects.filter(name=self.context["parent_operation"]).values('operation_id')[0]["operation_id"]
                return data
            except:
                raise serializers.ValidationError("Parent Operation DOES NOT exist!!")
        # check app_name & view_name
        return data
    class Meta:
        model = Operation
        fields = ('name', 'url', 'description', 'sub_operations')

class EditOperation(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    app_name = serializers.CharField(required=False)
    view_name = serializers.CharField(required=False)
    role_belong_to = serializers.CharField(required=False)
    parent_operation_id = serializers.IntegerField(required=False)
    class Meta:
        model = Operation
        fields = ('operation_id', 'name', 'app_name', 'view_name', 'role_belong_to', 'parent_operation_id')