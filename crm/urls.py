from django.urls import path
from . import views

app_name = 'crm'

urlpatterns = [
    path('leads/', views.lead_list, name='lead_list'),
    path('leads/create/', views.lead_create, name='lead_create'),
    path('leads/update/<int:lead_id>/', views.lead_update, name='lead_update'),
]
