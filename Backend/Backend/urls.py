# Backend/urls.py
# import from framework
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
# import from project
urlpatterns = [
    url('User/', include('User.urls', namespace='Users')),
    url('Station/', include('Station.urls', namespace='Station')),
    url('Route/', include('Route.urls', namespace='Route')),
    url('Menu/', include('Operation.urls', namespace='Menu')),
    url('Flow/', include('Flow.urls', namespace='Flow')),
    url('Combination/', include('Combination.urls', namespace='Combination')),
    path('admin/', admin.site.urls),
]
