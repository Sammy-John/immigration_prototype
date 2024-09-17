from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Lead

class LeadForm(forms.ModelForm):
    # Use PhoneNumberField to ensure proper validation
    phone = PhoneNumberField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+12125552368'  # Example of an international format
        }),
        label="Phone Number",
        help_text="Enter the phone number in international format (e.g., +12125552368)."
    )

    class Meta:
        model = Lead
        # Exclude 'status' from the form
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'inquiry_type',
            'subscribe_to_mailing_list',
            'notes'
        ]
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 4}),
        }
