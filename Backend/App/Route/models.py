# App/Route/models.py
# import from framework
from django.db import models
# import from project

class Route(models.Model):
    route_id = models.IntegerField(primary_key=True)
    route_name = models.CharField(max_length=20, default="")
    class Meta:
        permissions = (
                       ('can_view_route', 'Can View Route'),
                       ('can_edit_route', 'Can Edit Route'),
        )
    def __str__(self):
        return "Route " + str(self.route_id) + ": " + self.route_name