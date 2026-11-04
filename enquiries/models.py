from django.db import models
from properties.models import Property

class Enquiry(models.Model):

    ENQUIRY_TYPES = [
        ('General', 'General Enquiry'),
        ('Viewing', 'Property Viewing'),
        ('Buying', 'Buying a Property'),
        ('Renting', 'Renting a Property'),
    ]

    STATUS_CHOICES = [
        ('New', 'New'),
        ('Contacted', 'Contacted'),
        ('Resolved', 'Resolved'),
    ]

    property = models.ForeignKey(
        Property,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='enquiries'
    )

    full_name = models.CharField(max_length=150)

    email = models.EmailField()

    phone = models.CharField(max_length=20, blank=True)

    enquiry_type = models.CharField(
        max_length=20,
        choices=ENQUIRY_TYPES,
        default='General'
    )

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='New'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.enquiry_type}"

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Enquiries'