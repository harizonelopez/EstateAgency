from django.db import models

class Agent(models.Model):
    full_name = models.CharField(max_length=150)
    position = models.CharField(max_length=100, help_text="e.g. Senior Real Estate Agent")
    bio = models.TextField()
    photo = models.ImageField(upload_to='agents/')
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        ordering = ['full_name']
        verbose_name_plural = 'Agents'