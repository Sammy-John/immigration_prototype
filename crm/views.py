from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Lead
from django.contrib.auth.decorators import login_required
from .forms import LeadForm
from django.db import IntegrityError

def custom_login_required(view_func):
    """Custom decorator to add a message before redirecting to login."""
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'You must be logged in to access this page.')
            return redirect('login')  # Redirect to login URL
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
            lead.created_by = request.user  # Automatically assign the user creating the lead
            lead.updated_by = request.user  # Set the user who is initially updating/creating
            try:
                lead.save()
                messages.success(request, 'Lead created successfully.')
                return redirect('crm:lead_list')
            except IntegrityError:
                messages.error(request, 'A lead with this email or phone number already exists.')
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
            lead.updated_by = request.user  # Automatically assign the user updating the lead
            lead.save()
            messages.success(request, 'Lead updated successfully.')
            return redirect('crm:lead_list')
    else:
        form = LeadForm(instance=lead)
    return render(request, 'crm/lead_form.html', {'form': form})
