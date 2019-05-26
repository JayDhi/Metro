# Backend/urls.py
# import from framework
from django.contrib import admin
from django.urls import path
# import from project
from App.User.views import user_list, user_create
from App.Station.views import station_list, station_create
from App.Route.views import route_list, route_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_list/', user_list),
    path('user_create/', user_create),
    path('station_list/', station_list),
    path('station_create/', station_create),
    path('route_list/', route_list),
    path('route_create/', route_create),
]
