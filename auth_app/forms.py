from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import CustomUser

User = get_user_model()  # Get the custom user model

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class InternalUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'role', 'password1', 'password2')  # Include password fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['role'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))  # Use email field instead of username

    class Meta:
        model = CustomUser
        fields = ('username', 'password')  # Use username to represent email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Email"  # Rename label for clarity
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
