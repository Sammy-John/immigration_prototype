# dashboard/urls.py
from django.urls import path
from .views import dashboard_home

app_name = 'dashboard'  # Namespace for the app

urlpatterns = [
    path('', dashboard_home, name='home'),
]
