# App/Operation/urls.py
# import from framework
from django.urls import path
# import from project
from App.Operation import views

app_name="Operation"
urlpatterns = [
    path('get_user_menu/', views.get_user_menu, name='get_user_menu'),
    path('add_role/', views.update_role, name='update_role'),
]