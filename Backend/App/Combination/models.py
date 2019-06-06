# App/Combination/models
# import from framework
from django.db import models
# import from project
from App.Route.models import Route
from App.Station.models import Station

class RouteXStation(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    seq = models.IntegerField()
    station = models.ForeignKey(Station, on_delete=models.CASCADE)

    def __str__(self):
        return "No. " + str(self.seq) + " Station: " + self.station.station_name + " of Route: " + self.route.route_name

class UserFav(models.Model):
    fav_sites = models.BinaryField(blank=True, null=True)
    fav_routes = models.BinaryField(blank=True, null=True)
    fav_stations = models.BinaryField(blank=True, null=True)
    def __str__(self):
        return "User Fav"
# 用户常去的站点
# Class UserXStation

# 用户常去的地点
# Class UserXSite