# App/Operation/urls.py
# import from framework
from django.urls import path
# import from project
from App.Operation import views

app_name="Operation"
urlpatterns = [
    path('get_menu/', views.get_menu, name='get_menu'),
    path('edit_menu/', views.edit_menu, name='edit_menu'),
]