# App/Station/models.py
# import from framework
from django.db import models
# import from project

class Station(models.Model):
    station_id = models.IntegerField(primary_key=True)
    station_name = models.CharField(max_length=20, default="", unique=True)
    station_x_cor = models.IntegerField(default=0)
    station_y_cor = models.IntegerField(default=0)
    class Meta:
        permissions = (
                       ('can_view_station', 'Can View Station'),
                       ('can_edit_station', 'Can Edit Station'),
        )
    def __str__(self):
        return self.station_name