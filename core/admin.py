from django.contrib import admin
from .models import Service, Testimonial

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_active',
        'display_order',
        'created_at',
    )

    list_filter = ('is_active',)
    search_fields = ('title', 'short_description')
    prepopulated_fields = {
        'slug': ('title',)
    }

    ordering = ('display_order', 'title')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'client_name',
        'client_role',
        'rating',
        'is_active',
        'created_at',
    )

    list_filter = ('rating', 'is_active')
    search_fields = ('client_name', 'client_role', 'message')
    list_editable = ('is_active',)
    ordering = ('-created_at',)