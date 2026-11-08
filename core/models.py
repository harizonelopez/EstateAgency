from django.db import models
from django.utils.text import slugify

class Service(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(
        max_length=120,
        unique=True,
        blank=True
    )

    short_description = models.CharField(max_length=250)
    description = models.TextField()
    icon = models.CharField(
        max_length=50,
        default='bi-house'
    )

    image = models.ImageField(
        upload_to='services/'
    )

    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['display_order', 'title']
        verbose_name_plural = 'Services'

class Testimonial(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    client_name = models.CharField(max_length=50)
    client_role = models.CharField(max_length=50, blank=True)
    message = models.TextField()

    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES,
        default=5
    )

    photo = models.ImageField(
        upload_to='testimonials/',
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Testimonials'