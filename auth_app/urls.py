from django.urls import path
from .views import login_view, logout_view, create_internal_user_view, no_permission_view

app_name = 'auth_app'  # Make sure the namespace is defined

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('create-user/', create_internal_user_view, name='create_internal_user'),
    path('no-permission/', no_permission_view, name='no_permission'),
]
