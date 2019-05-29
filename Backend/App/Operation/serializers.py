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
            return [OperationSerializer(i).data for i in Operation.objects.filter(parent_operation_id=obj.operation_id)]
        except:
            traceback.print_exc()
            return None
    class Meta:
        model = Operation
        fields = ('name', 'url', 'description', 'sub_operations')