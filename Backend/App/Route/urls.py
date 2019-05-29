# App/Route/urls.py
# import from framework
from django.urls import path
# import from project
from App.Route import views

app_name="Route"
urlpatterns = [
    path('list_route/', views.route_list, name='list_route'),
    path('add_route/', views.route_create, name='add_route'),
]