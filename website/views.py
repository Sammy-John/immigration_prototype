from django.shortcuts import render, redirect
from crm.models import Lead  
from .forms import ContactForm
from django.contrib import messages
from django.db import IntegrityError

def home_view(request):
    """View for the home page."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Combine the country code and phone number
            phone_number = form.cleaned_data['phone_number']

            # Check for an existing lead with the same email
            email = form.cleaned_data['email']
            if Lead.objects.filter(email=email).exists():
                messages.error(request, 'This email is already associated with an existing lead.')
                return render(request, 'website/home.html', {'form': form})

            # Save the form data to create a new lead in the CRM app
            try:
                Lead.objects.create(
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    email=email,
                    phone=phone_number,
                    inquiry_type=form.cleaned_data['reason'],
                    notes=form.cleaned_data['message'],
                    created_by_id=0  # ID for website as default source
                )
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('website:contact_success')
            except IntegrityError as e:
                messages.error(request, 'There was a problem saving your contact. Please try again later.')
                return render(request, 'website/home.html', {'form': form})
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    return render(request, 'website/home.html', {'form': form})

def about_view(request):
    """View for the about page."""
    return render(request, 'website/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Combine the country code and phone number
            phone_number = form.cleaned_data['phone_number']

            # Check for an existing lead with the same email
            email = form.cleaned_data['email']
            if Lead.objects.filter(email=email).exists():
                messages.error(request, 'This email is already associated with an existing lead.')
                return render(request, 'website/contact.html', {'form': form})

            # Save the form data to create a new lead in the CRM app
            try:
                Lead.objects.create(
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    email=email,
                    phone=phone_number,
                    inquiry_type=form.cleaned_data['reason'],
                    notes=form.cleaned_data['message'],
                    created_by_id=0  # ID for website as default source
                )
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('website:contact_success')
            except IntegrityError as e:
                messages.error(request, 'There was a problem saving your contact. Please try again later.')
                return render(request, 'website/contact.html', {'form': form})
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})

def contact_success(request):
    """View for the contact success page."""
    return render(request, 'website/contact_success.html')


def services_individuals_view(request):
    """View for the Services for Individuals page."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            if Lead.objects.filter(email=email).exists():
                messages.error(request, 'This email is already associated with an existing lead.')
                return render(request, 'website/services_individuals.html', {'form': form})

            try:
                Lead.objects.create(
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    email=email,
                    phone=phone_number,
                    inquiry_type=form.cleaned_data['reason'],
                    notes=form.cleaned_data['message'],
                    created_by_id=0  # ID for website as default source
                )
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('website:contact_success')
            except IntegrityError as e:
                messages.error(request, 'There was a problem saving your contact. Please try again later.')
                return render(request, 'website/services_individuals.html', {'form': form})
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    return render(request, 'website/services_individuals.html', {'form': form})
