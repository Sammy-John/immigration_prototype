from django.db import models
from django.contrib.auth import get_user_model

class Lead(models.Model):
    # Fields for the Lead model
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)  # Unique constraint for duplicate prevention
    phone = models.CharField(max_length=20, unique=True)
    
    source = models.CharField(
        max_length=50,
        choices=[
            ('office_user', 'Office User'),  # Entered manually by office staff
            ('website', 'Website Form'),     # Captured via the website form
            ('email', 'Email'),              # Generated from email inquiry
            ('phone', 'Phone Call'),         # Entered manually from a phone call
            ('whatsapp', 'WhatsApp'),        # Entered manually from a WhatsApp message
        ],
        default='website',
        help_text='Describes how the lead was created or the source of creation.'
    )
    
    inquiry_type = models.CharField(
        max_length=50,
        choices=[
            ('work_visa', 'Work Visa'),
            ('student_visa', 'Student Visa'),
            ('visitor_visa', 'Visitor Visa'),
            ('family_visa', 'Family Visa'),
            ('residency_visa', 'Residency Visa'),
            ('investment_visa', 'Investment or Business Visa'),
            ('other', 'Other'),
        ]
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('new', 'New'),
            ('contacted', 'Contacted'),
            ('dismissed', 'Dismissed'),
            ('converted', 'Converted to Contact'),
        ],
        default='new'
    )

    subscribe_to_mailing_list = models.BooleanField(
        default=False,
        help_text='Indicates if the lead wants to subscribe to the mailing list for marketing emails.'
    )
    
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_leads',  # Add related_name for reverse accessor
        help_text='User who created the lead. Could be an internal user or left blank if created externally.'
    )
    notes = models.TextField(
        blank=True,
        help_text='Additional information or context about the lead (e.g., details from a phone call, email, or form submission).'
    )

    assigned_agent = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_leads',  # Add related_name for reverse accessor
        help_text='Agent responsible for managing the lead. Can be null if unassigned.'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def convert_to_contact(self):
        # Logic for converting a lead to a contact...
        pass
