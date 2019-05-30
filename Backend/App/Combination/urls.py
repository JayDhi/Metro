# App/Combination/urls.py
# import from framework
from django.urls import path
# import from project
from App.Combination import views

app_name = "Route"
urlpatterns = [
    path('list_route_map/', views.route_seq_list, name='list_route_map'),
    path('edit_route_map/', views.route_seq_create, name='edit_route_map'),
]