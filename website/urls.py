from django.urls import path
from django.views.generic import RedirectView
from .views import home_view, about_view, contact_view, contact_success, services_individuals_view, employers_view, blog_view, blog_detail_view


app_name = 'website'

urlpatterns = [
    path('', home_view, name='home'),  # Homepage for the website app
    path('login/', RedirectView.as_view(pattern_name='auth_app:login', permanent=False), name='login_redirect'),  # Redirect to the login page
    path('about/', about_view, name='about'),  # About page
    path('contact/', contact_view, name='contact'),  # Contact page
    path('contact/success/', contact_success, name='contact_success'),  # Contact Success page
    path('services/individuals/', services_individuals_view, name='services_individuals'),  # Services for Individuals page
    path('employers/', employers_view, name='employers'),
    path('blog/', blog_view, name='blog'),  # Blog page
    path('blog/<int:post_id>/', blog_detail_view, name='blog_detail'),
]
