from django.urls import path
from . import views

urlpatterns = [
    path('healthcheck', views.healthcheck, name='api_healthcheck'),
]
