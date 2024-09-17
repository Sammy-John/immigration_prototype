from django.urls import path
from . import views

app_name = 'cms'

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('pages/', views.manage_pages, name='manage_pages'),
    path('posts/', views.manage_posts, name='manage_posts'),
    path('services/', views.manage_services, name='manage_services'),
    path('contact/', views.manage_contact, name='manage_contact'),
    path('assets/', views.manage_assets, name='manage_assets'),
]
