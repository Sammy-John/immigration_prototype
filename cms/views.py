from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def cms_dashboard(request):
    # Your CMS logic here
    return render(request, 'cms/dashboard.html')

def dashboard_view(request):
    return render(request, 'cms/dashboard.html')

def manage_pages(request):
    # Logic to manage pages will go here
    return render(request, 'cms/manage_pages.html')

def manage_posts(request):
    # Logic to manage posts will go here
    return render(request, 'cms/manage_posts.html')

def manage_services(request):
    # Logic to manage services will go here
    return render(request, 'cms/manage_services.html')

def manage_contact(request):
    # Logic to manage contact information will go here
    return render(request, 'cms/manage_contact.html')

def manage_assets(request):
    # Logic to manage assets will go here
    return render(request, 'cms/manage_assets.html')
