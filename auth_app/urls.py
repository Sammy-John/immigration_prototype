from django.urls import path
from .views import (
    login_view,
    logout_view,
    create_internal_user_view,
    no_permission_view,
    user_list_view,  # New view for listing users
    edit_user_view,  # New view for editing users
    deactivate_user_view,  # New view for deactivating users
    reactivate_user_view  # New view for reactivating users
)

app_name = 'auth_app'  # Define the namespace for the app

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('create-user/', create_internal_user_view, name='create_internal_user'),
    path('no-permission/', no_permission_view, name='no_permission'),
    path('users/', user_list_view, name='user_list'),  # URL for managing users
    path('users/edit/<int:user_id>/', edit_user_view, name='edit_user'),  # URL for editing users
    path('users/deactivate/<int:user_id>/', deactivate_user_view, name='deactivate_user'),  # URL for deactivating users
    path('users/reactivate/<int:user_id>/', reactivate_user_view, name='reactivate_user'),  # URL for reactivating users
]
