from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import InternalUserCreationForm, CustomAuthenticationForm
from .models import CustomUser, UserAuditLog

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Redirect all users to the dashboard after login
            return redirect('dashboard:home')
        else:
            messages.error(request, 'Invalid email or password.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'auth_app/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('auth_app:login')  # Use namespace for login URL

def is_manager_or_super_admin(user):
    return user.role in ['manager', 'super_admin']

@login_required
@user_passes_test(is_manager_or_super_admin, login_url='auth_app:login', redirect_field_name=None)
def create_internal_user_view(request):
    print("User trying to access create user page:", request.user.email)
    
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
                changed_by=request.user
            )

            messages.success(request, 'New user account has been created with a password.')
            return redirect('auth_app:create_internal_user')  # Use namespace here
    else:
        print("GET request for create user page")
        form = InternalUserCreationForm()
    return render(request, 'auth_app/create_internal_user.html', {'form': form})

@login_required
def no_permission_view(request):
    messages.error(request, 'You do not have permission to access this page.')
    return render(request, 'auth_app/no_permission.html')

@login_required
@user_passes_test(lambda u: u.role in ['manager', 'super_admin'], login_url='auth_app:login')
def user_list_view(request):
    """View to display a list of all users with management options."""
    users = CustomUser.objects.all()
    return render(request, 'auth_app/user_list.html', {'users': users})

@login_required
@user_passes_test(lambda u: u.role in ['manager', 'super_admin'], login_url='auth_app:login')
def edit_user_view(request, user_id):
    """View for editing a user's details."""
    user = get_object_or_404(CustomUser, pk=user_id)
    if request.method == 'POST':
        form = InternalUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User details updated successfully.')
            return redirect('auth_app:user_list')
    else:
        form = InternalUserCreationForm(instance=user)
    return render(request, 'auth_app/edit_user.html', {'form': form, 'user': user})

@login_required
@user_passes_test(lambda u: u.role in ['manager', 'super_admin'], login_url='auth_app:login')
def deactivate_user_view(request, user_id):
    """View for deactivating a user."""
    user = get_object_or_404(CustomUser, pk=user_id)
    user.is_active = False
    user.save()
    messages.success(request, f'User {user.username} has been deactivated.')
    return redirect('auth_app:user_list')

@login_required
@user_passes_test(lambda u: u.role in ['manager', 'super_admin'], login_url='auth_app:login')
def reactivate_user_view(request, user_id):
    """View for reactivating a user."""
    user = get_object_or_404(CustomUser, pk=user_id)
    user.is_active = True
    user.save()
    messages.success(request, f'User {user.username} has been reactivated.')
    return redirect('auth_app:user_list')
