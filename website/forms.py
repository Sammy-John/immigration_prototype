# website/forms.py
from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(
        max_length=50, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=50, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    phone_number = forms.CharField(
        max_length=20, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_phone_number'})
    )
    
    REASON_CHOICES = [
        ('complex_immigration', 'Complex Immigration Matters'),
        ('employer_assistance', 'Employer Assistance'),
        ('family_visa', 'Family Visa'),
        ('ppi_response', 'PPI Response'),
        ('residence_visa', 'Residence Visa'),
        ('student_visa', 'Student Visa'),
        ('visitor_visa', 'Visitor Visa'),
        ('work_to_residence', 'Work to Residence Visa'),
        ('arrange_consultation', 'Arrange a Consultation'),
        ('payment_issues', 'Payment Issues'),
        ('document_upload', 'Document Upload Assistance'),
        ('status_check', 'Application Status Check'),
        ('feedback_complaint', 'Feedback or Complaint'),
        ('general_inquiry', 'General Inquiry'),
        ('other', 'Other')
    ]
    reason = forms.ChoiceField(
        choices=REASON_CHOICES, 
        required=True, 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    message = forms.CharField(
        required=True, 
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'rows': 5, 
            'placeholder': 'Please provide any additional details...'
        })
    )
