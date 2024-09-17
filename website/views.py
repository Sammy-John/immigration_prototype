from django.shortcuts import render, redirect
from crm.models import Lead  # Assuming Lead is the model used to store form data
from .forms import ContactForm
from django.contrib import messages

def home_view(request):
    """View for the home page."""
    return render(request, 'website/home.html')

def about_view(request):
    """View for the about page."""
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Combine the country code and phone number
            phone_number = form.cleaned_data['phone_number']

            # Save the form data to create a new lead in the CRM app
            Lead.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                phone=phone_number,
                inquiry_type=form.cleaned_data['reason'],
                notes=form.cleaned_data['message']
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('website:contact_success')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})