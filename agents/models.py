from django.db import models

class Agent(models.Model):
    full_name = models.CharField(max_length=45)
    position = models.CharField(max_length=80, help_text="e.g. Senior Real Estate Agent")
    bio = models.TextField()
    years_experience = models.PositiveIntegerField(default=0, help_text="Number of years of professional experience")
    achievements = models.TextField(blank=True, help_text="Awards, accomplishments and professional milestones")
    specializations = models.TextField(blank=True, help_text="Areas of expertise and specialization")
    services = models.ManyToManyField('core.Service', blank=True, related_name='agents', help_text="Services offered by the agent")
    photo = models.ImageField(upload_to='agents/')
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
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