from django.shortcuts import render, redirect
from crm.models import Lead  
from .forms import ContactForm
from django.contrib import messages
from django.db import IntegrityError
from datetime import date

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

from django.shortcuts import render

def about_view(request):
    # Hardcoded team members for testing
    team_members = [
        {
            'name': 'John Doe',
            'position': 'CEO',
            'photo': 'website/images/team-member1.jpg',
            'bio': 'John has over 20 years of experience in the immigration industry, leading our team with passion and dedication.',
            'licence_number': 'L123456',
            'languages_spoken': 'English, Spanish',
            'email': 'john.doe@example.com',
            'education': 'MBA in Business Management'
        },
        {
            'name': 'Jane Smith',
            'position': 'Chief Legal Officer',
            'photo': 'website/images/team-member2.jpg',
            'bio': 'Jane specializes in immigration law and has successfully represented numerous clients in complex cases.',
            'licence_number': 'L789012',
            'languages_spoken': 'English, Mandarin',
            'email': 'jane.smith@example.com',
            'education': 'LLB in Law'
        },
        {
            'name': 'Alice Brown',
            'position': 'Head of Client Services',
            'photo': 'website/images/team-member3.jpg',
            'bio': 'Alice is dedicated to ensuring our clients receive the best service and support throughout their immigration journey.',
            'licence_number': None,  # No licence number
            'languages_spoken': 'English, French',
            'email': 'alice.brown@example.com',
            'education': 'BA in Communications'
        }
    ]

    return render(request, 'website/about.html', {'team_members': team_members})

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

def employers_view(request):
    """View for the Employers page."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            if Lead.objects.filter(email=email).exists():
                messages.error(request, 'This email is already associated with an existing lead.')
                return render(request, 'website/employers.html', {'form': form})

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
                return render(request, 'website/employers.html', {'form': form})
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    return render(request, 'website/employers.html', {'form': form})

def blog_view(request):
    """View for the Blog page with mock data."""
    # Mock data representing blog posts
    blog_posts = [
        {
            'id': 1,
            'title': 'Understanding New Zealand Visa Options',
            'author': 'John Doe',
            'date': date(2024, 9, 1),
            'excerpt': 'Explore various visa options available for moving to New Zealand...',
            'image': 'website/images/blog-image-1.jpg',
        },
        {
            'id': 2,
            'title': 'How to Prepare for Visa Application',
            'author': 'Jane Smith',
            'date': date(2024, 9, 5),
            'excerpt': 'Learn about the essential documents and steps required for a successful visa application...',
            'image': 'website/images/blog-image-2.jpg',
        },
        {
            'id': 3,
            'title': 'Common Mistakes to Avoid in Visa Applications',
            'author': 'Emma Brown',
            'date': date(2024, 9, 10),
            'excerpt': 'Avoid common pitfalls that can lead to visa application rejection...',
            'image': 'website/images/blog-image-3.jpg',
        }
    ]

    return render(request, 'website/blog.html', {'blog_posts': blog_posts})

def blog_detail_view(request, post_id):
    """View for an individual blog post."""
    # Mock data representing a single blog post
    mock_post = {
        'id': post_id,
        'title': 'Understanding New Zealand Visa Options',
        'author': 'John Doe',
        'date': date(2024, 9, 1),
        'content': '''
            In this post, we will discuss the different visa options available for those looking to move to New Zealand. 
            Whether you are planning to study, work, or join family, there are several visa categories to consider...
            ''',
        'image': 'website/images/blog-image-1.jpg',
    }

    return render(request, 'website/blog_detail.html', {'post': mock_post})