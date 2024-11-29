from django.contrib import admin
from .models import Applicant

# Register your models here.
@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name','last_name', 'email', 'phone', 'resume', 'education', 'linked_in_profile', 'portfolio_link', 'address')
    search_fields = ('user', 'first_name', 'email', 'phone', 'education')
    list_filter = ('user', 'first_name', 'email', 'phone', 'education')


class ApplicantSite(admin.AdminSite):
    site_header = 'Application Admin'
    site_title = site_header
    index_title = 'Application Management'
    
    
from django.contrib import admin
from django.utils.html import format_html
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    # List display options for the model in the admin interface
    list_display = ('applicant', 'job', 'status', 'application_date', 'interview', 'submitted_date', 'view_cover_letter')

    # Adding filters for easier search and filtering in the admin interface
    list_filter = ('status', 'job', 'application_date', 'interview')
    
    # Adding search fields to allow searching by applicant name and job title
    search_fields = ('applicant__user__username', 'job__title')

    # Configure the fieldsets to organize fields in a logical order
    fieldsets = (
        (None, {
            'fields': ('applicant', 'job', 'status', 'cover_letter', 'additional_documents')
        }),
        ('Additional Information', {
            'fields': ('notes', 'interview', 'submitted_date'),
        }),
    )

    # Customize the form to include a link to view the cover letter in the admin interface
    def view_cover_letter(self, obj):
        if obj.cover_letter:
            return format_html('<a href="{}" target="_blank">View Cover Letter</a>', obj.cover_letter.url)
        return 'No Cover Letter'
    view_cover_letter.short_description = 'Cover Letter'

    # Define a custom save method if needed (e.g., you might want to log or manipulate data before saving)
    def save_model(self, request, obj, form, change):
        # You can add custom save behavior here
        super().save_model(request, obj, form, change)

    # Customize ordering in the admin list view
    ordering = ('-application_date',)
