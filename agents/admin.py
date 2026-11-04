from django.contrib import admin
from .models import Agent
@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'position',
        'email',
        'phone',
        'is_active',
    )

    list_filter = ('is_active',)

    search_fields = (
        'full_name',
        'email',
        'phone',
    )