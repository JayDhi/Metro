# App/Site/models.py
# import from framework
from django.db import models
# import from project

class Site(models.Model):
    site_id = models.IntegerField(primary_key=True)
    site_name = models.CharField(max_length=20, default="")
    site_description = models.CharField(max_length=50, default="")
    site_x_cor = models.IntegerField(default="")
    site_y_cor = models.IntegerField(default="")
    site_fav_rate = models.IntegerField(default=0)
    def __str__(self):
        return "site name: "+self.site_name+'\n'+"site description: "+self.site_description