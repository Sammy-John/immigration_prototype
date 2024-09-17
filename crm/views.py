from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db import connections
from django.db.utils import DatabaseError
from django.contrib.auth import get_user_model
from .models import Lead
from .forms import LeadForm

User = get_user_model()

def custom_login_required(view_func):
    """Custom decorator to add a message before redirecting to login."""
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'You must be logged in to access this page.')
            return redirect('auth_app:login')  # Use the 'auth_app' namespace
        return view_func(request, *args, **kwargs)
    return wrapper


@custom_login_required
def lead_list(request):
    """View to display a list of all leads."""
    leads = Lead.objects.all()
    return render(request, 'crm/lead_list.html', {'leads': leads})

@custom_login_required
def lead_create(request):
    """View to create a new lead."""
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)

            # Correctly set the IDs
            lead.created_by_id = request.user.id
            lead.updated_by_id = request.user.id

            try:
                # Save to crm_db
                lead.save(using='crm_db')
                messages.success(request, 'Lead created successfully.')
                return redirect('crm:lead_list')
            except IntegrityError as e:
                print("Database error:", e)  # Debugging print
                messages.error(request, 'A database error occurred while saving the lead.')
        else:
            print("Form errors:", form.errors)  # Debugging print
            messages.error(request, 'Please correct the errors below.')
    else:
        form = LeadForm()

    return render(request, 'crm/lead_form.html', {'form': form})

@custom_login_required
def lead_update(request, lead_id):
    """View to update an existing lead."""
    lead = get_object_or_404(Lead, pk=lead_id)
    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.updated_by_id = request.user.id  # Use the user ID to avoid cross-database issues
            lead.save()
            messages.success(request, 'Lead updated successfully.')
            return redirect('crm:lead_list')
    else:
        form = LeadForm(instance=lead)
    return render(request, 'crm/lead_form.html', {'form': form})
