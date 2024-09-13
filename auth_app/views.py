from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import InternalUserCreationForm, CustomAuthenticationForm
from .models import CustomUser, UserAuditLog  # Import the models

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            # Check the user's role and redirect accordingly
            if user.role in ['manager', 'super_admin']:
                return redirect('create_internal_user')  # Redirect to create user page for authorized users
            else:
                messages.error(request, 'You do not have permission to access the user creation page.')
                return redirect('no_permission')  # Redirect to a page or render a template explaining lack of permissions
                
        else:
            messages.error(request, 'Invalid email or password.')  # Show error if login fails
    else:
        form = CustomAuthenticationForm()
    return render(request, 'auth_app/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

def is_manager_or_super_admin(user):
    return user.role in ['manager', 'super_admin']

@login_required
@user_passes_test(is_manager_or_super_admin, login_url='login', redirect_field_name=None)
def create_internal_user_view(request):
    print("User trying to access create user page:", request.user.email)  # Debugging statement
    
    if request.method == 'POST':
        form = InternalUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            raw_password = form.cleaned_data.get('password1')  # Get the password from the form
            user.set_password(raw_password)  # Set the user's password properly

            # Save the new user instance
            user.save()

            # Log the creation of the new user manually
            UserAuditLog.objects.create(
                user=user,
                action='created',
                changed_by=request.user  # Properly log who created the user
            )

            messages.success(request, 'New user account has been created with a password.')
            return redirect('create_internal_user')  # Temporary redirect to create user page
    else:
        print("GET request for create user page")  # Debugging statement
        form = InternalUserCreationForm()
    return render(request, 'auth_app/create_internal_user.html', {'form': form})

@login_required
def no_permission_view(request):
    messages.error(request, 'You do not have permission to access this page.')
    return render(request, 'auth_app/no_permission.html')
