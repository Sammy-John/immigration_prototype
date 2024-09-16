# website/urls.py
from django.urls import path
from django.views.generic import RedirectView
from .views import home_view, about_view, contact_view

app_name = 'website'

urlpatterns = [
    path('', home_view, name='home'),  # Homepage for the website app
    path('login/', RedirectView.as_view(pattern_name='auth_app:login', permanent=False), name='login_redirect'),  # Redirect to the login page
    path('about/', about_view, name='about'),  # About page
    path('contact/', contact_view, name='contact'),  # Contact page
]
