from django.db import models
from django.utils.text import slugify

class Property(models.Model):

    PROPERTY_TYPES = [
        ('Apartment', 'Apartment'),
        ('House', 'House'),
        ('Villa', 'Villa'),
        ('Land', 'Land'),
        ('Commercial', 'Commercial'),
    ]

    LISTING_TYPES = [
        ('Sale', 'For Sale'),
        ('Rent', 'For Rent'),
    ]

    title = models.CharField(max_length=80)
    slug = models.SlugField(unique=True, blank=True)
    property_id = models.CharField(max_length=5, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)

    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_TYPES
    )

    listing_type = models.CharField(
        max_length=10,
        choices=LISTING_TYPES
    )

    location = models.CharField(max_length=50)
    area = models.DecimalField(max_digits=4, decimal_places=2)
    bedrooms = models.PositiveIntegerField(default=0)
    bathrooms = models.PositiveIntegerField(default=0)
    garages = models.PositiveIntegerField(default=0)

    main_image = models.ImageField(upload_to='properties/')

    is_featured = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Properties'

class PropertyImage(models.Model):

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.ImageField(upload_to='properties/gallery/')
    alt_text = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.property.title}"
    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Property Images'