# Backend/urls.py
# import from framework
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
# import from project
from App.User.views import user_list, user_create
from App.Station.views import station_list, station_create
from App.Route.views import route_list, route_create
from App.Combination.views import route_seq_list, route_seq_create
urlpatterns = [
    path('token/obtain/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('admin/', admin.site.urls),
    path('user_list/', user_list),
    path('user_create/', user_create),
    path('station_list/', station_list),
    path('station_create/', station_create),
    path('route_list/', route_list),
    path('route_create/', route_create),
    path('route_seq_list/', route_seq_list),
    path('route_seq_create/', route_seq_create),
]
