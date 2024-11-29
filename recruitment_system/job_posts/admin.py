from django.contrib import admin
from .models import Job

# Register your models here.
@admin.register(Job)
class JobFields(admin.ModelAdmin):
    list_display = ('title', 'company', 'job_level', 'employment_type', 'location', 'posted_date', 'application_deadline','job_status')
    search_fields = ( 'company__name', 'job_function', 'location')
    list_filter = ('title','company__name', 'job_level', 'employment_type', 'education', 'posted_date')
    
class JobAdmin(admin.AdminSite):
    site_header = 'Job Admin'
    site_title = site_header
    index_title = 'Job Management'

job_admin = JobAdmin(name='job-admin')
job_admin.register(Job, JobFields)
