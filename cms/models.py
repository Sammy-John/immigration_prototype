from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class PageSection(models.Model):
    """Model to represent different sections of pages that can be edited."""
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Service(models.Model):
    """Model to represent services that the website offers."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='service_icons/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    """Model to represent blog posts."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ContactDetail(models.Model):
    """Model to represent contact details for the website."""
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    type = models.CharField(
        max_length=50,
        choices=[('email', 'Email'), ('phone', 'Phone'), ('address', 'Address')]
    )

    def __str__(self):
        return f"{self.name} ({self.type})"
