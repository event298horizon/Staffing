from django.contrib import admin
from .models import Job
# Register your models here.

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company_name', 'location', 'approved')
    list_filter = ('approved', 'location')
    search_fields = ('job_title', 'company_name')
