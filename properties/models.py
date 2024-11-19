from django.db import models
from accounts.models import User

class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('commercial', 'Commercial'),
        ('hotel', 'Hotel'),
        ('rent', 'Rent')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES, blank=True, null=True)
    price = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    size = models.PositiveIntegerField(help_text="Size in square meters", blank=True, null=True)
    number_of_rooms = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='property_images/', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title