# App/Station/urls.py
# import from framework
from django.urls import path
# import from project
from App.Station import views

app_name="Station"
urlpatterns = [
    path('get_station/', views.get_station, name='list_station'),
    path('edit_station/', views.edit_station, name='add_station'),
]