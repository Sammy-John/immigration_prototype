from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
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
