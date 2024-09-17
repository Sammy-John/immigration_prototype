from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    phone_number = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    REASON_CHOICES = [
        ('work_visa', 'Work Visa'),
        ('student_visa', 'Student Visa'),
        ('visitor_visa', 'Visitor Visa'),
        ('family_visa', 'Family Visa'),
        ('residency_visa', 'Residency Visa'),
        ('investment_visa', 'Investment or Business Visa'),
        ('other', 'Other')
    ]
    reason = forms.ChoiceField(choices=REASON_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Please provide any additional details...'}))
