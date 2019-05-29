# Backend/urls.py
# import from framework
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
# import from project
from App.User.utils import MyTokenObtainPairView
from App.User.views import user_list, user_create, test, view_profile
from App.Station.views import station_list, station_create
from App.Route.views import route_list, route_create
from App.Combination.views import route_seq_list, route_seq_create
urlpatterns = [
    url('User/', include('User.urls', namespace='Users')),
    url('Station/', include('Station.urls', namespace='Station')),
    url('Route/', include('Route.urls', namespace='Route')),
    url('Menu/', include('Operation.urls', namespace='Menu')),
    path('token/obtain/', MyTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('admin/', admin.site.urls),
    path('test/', test),
]
