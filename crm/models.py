from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()

class Lead(models.Model):
    """Model to represent potential leads for services."""

    # Define a constant for the "website" ID
    WEBSITE_USER_ID = 0

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField()

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

    created_by_id = models.IntegerField(
        default=WEBSITE_USER_ID,
        help_text='ID of the user who created the lead. Default is 0 for website.'
    )

    updated_by = models.ForeignKey(
        User,
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
        # Automatically set created_by_id to WEBSITE_USER_ID if not already set
        if self.created_by_id is None:
            self.created_by_id = self.WEBSITE_USER_ID
        super().save(*args, **kwargs)

    @property
    def created_by_display(self):
        """Return 'Website' if created_by_id is 0, otherwise the username."""
        if self.created_by_id == self.WEBSITE_USER_ID:
            return "Website"
        else:
            try:
                user = User.objects.get(id=self.created_by_id)
                return user.get_full_name() or user.email
            except User.DoesNotExist:
                return "Unknown"
