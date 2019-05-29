# App/Operation/models.py
# import from framework
from django.db import models
# import from project

class Operation(models.Model):
    operation_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, default="", unique=True)
    description = models.CharField(max_length=50, default="")
    app_name = models.CharField(max_length=20, default="")
    view_name = models.CharField(max_length=20, default="")
    parent_operation = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    role_belong_to = models.CharField(max_length=4, default="3")

    def __str__(self):
        return self.name