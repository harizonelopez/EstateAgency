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