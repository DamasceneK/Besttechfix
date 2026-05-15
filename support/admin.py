from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'device_type', 'location', 'created_at', 'completed')
    list_filter = ('device_type', 'completed', 'created_at')
    search_fields = ('name', 'phone', 'email', 'location', 'issue_description')