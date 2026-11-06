from django.contrib import admin
from .models import Agent

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'position',
        'years_experience',
        'phone',
        'email',
        'is_active',
    )

    list_filter = (
        'is_active',
        'years_experience',
    )

    search_fields = (
        'full_name',
        'position',
        'email',
        'phone',
    )

    filter_horizontal = ('services',)

    fieldsets = (
        ('Basic Information', {
            'fields': (
                'full_name',
                'position',
                'bio',
                'photo',
            )
        }),

        ('Professional Profile', {
            'fields': (
                'years_experience',
                'specializations',
                'achievements',
                'services',
            )
        }),

        ('Contact Information', {
            'fields': (
                'email',
                'phone',
            )
        }),

        ('Social Media', {
            'fields': (
                'facebook',
                'instagram',
                'linkedin',
                'twitter',
            )
        }),

        ('Account Status', {
            'fields': ('is_active',)
        }),

        ('System Information', {
            'fields': (
                'created_at',
                'updated_at',
            ),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )