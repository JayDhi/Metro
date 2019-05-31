# App/Route/urls.py
# import from framework
from django.urls import path
# import from project
from App.Route import views

app_name="Route"
urlpatterns = [
    path('get_route/', views.get_route, name='get_route'),
    path('edit_route/', views.edit_route, name='edit_route'),
]