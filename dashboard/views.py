from django.shortcuts import render

def dashboard_home(request):
    """View for the dashboard home page."""
    return render(request, 'dashboard/home.html')
