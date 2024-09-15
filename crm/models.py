from django.db import models
from django.contrib.auth import get_user_model

class Lead(models.Model):
    """Model to represent potential leads for services."""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)

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
        related_name='created_leads',
        help_text='User who created the lead.'
    )

    updated_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='updated_leads',
        help_text='User who last updated the lead.',
        editable=False
    )

    notes = models.TextField(
        blank=True,
        help_text='Additional information or context about the lead (e.g., details from a phone call, email, or form submission).'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

    def save(self, *args, **kwargs):
        # Automatically set the user who made the last update
        if 'request' in kwargs:
            request = kwargs.pop('request')
            if not self.created_by:
                self.created_by = request.user
            self.updated_by = request.user

        super().save(*args, **kwargs)
