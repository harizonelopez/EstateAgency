from django.contrib import admin
from .models import Enquiry

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'email',
        'phone',
        'enquiry_type',
        'property',
        'status',
        'created_at',
    )

    list_filter = (
        'enquiry_type',
        'status',
        'created_at',
    )

    search_fields = (
        'full_name',
        'email',
        'phone',
        'message',
    )

    readonly_fields = ('created_at',)

    date_hierarchy = 'created_at'