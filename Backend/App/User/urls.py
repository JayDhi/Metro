# App/User/urls.py
# import from framework
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
# import from project
from App.User import views, utils

app_name = "User"
urlpatterns = [
    path('obtain_token/', utils.MyTokenObtainPairView.as_view(), name='obtain_token'),
    path('refresh_token/',  TokenRefreshView.as_view(), name='refresh_token'),
    path('get_profile/', views.view_profile, name='view_profile'),
]