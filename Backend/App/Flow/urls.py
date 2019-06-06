# App/Flow/urls.py
# import from framework
from django.urls import path
# import from project
from App.Flow import views

app_name="Operation"
urlpatterns = [
    path('show_flow/', views.show_flow, name='show_flow_data'),
]