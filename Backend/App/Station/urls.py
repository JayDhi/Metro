# App/Station/urls.py
# import from framework
from django.urls import path
# import from project
from App.Station import views

app_name="Station"
urlpatterns = [
    path('list_station/', views.station_list, name='list_station'),
    path('add_station/', views.station_create, name='add_station'),
]