from django.contrib import admin
from .models import Property, PropertyImage

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'property_id',
        'property_type',
        'listing_type',
        'price',
        'location',
        'is_available',
        'is_featured',
    )

    list_filter = (
        'property_type',
        'listing_type',
        'is_available',
        'is_featured',
    )

    search_fields = (
        'title',
        'property_id',
        'location',
    )

    prepopulated_fields = {
        'slug': ('title',)
    }

    inlines = [PropertyImageInline]

@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ('property', 'alt_text', 'created_at')
    search_fields = ('property__title', 'alt_text')