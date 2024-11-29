from django.contrib import admin
from .models import Company, CompanyInfo, Branch, Employee

@admin.register(Company)
class CompanyFields(admin.ModelAdmin):
    list_display = ('name', 'logo', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('name',)
#    list_editable = ('name',)
    ordering = ('name',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')

@admin.register(CompanyInfo)
class CompanyInfoFields(admin.ModelAdmin):
    list_display = ('company', 'company_owner','industry', 'email', 'phone_number', 'established', 'employees', 'revenue', 'headquarters', 'founded_by', 'number_of_branches', 'website', 'description')
    list_filter = ('headquarters', 'founded_by', 'employees', 'founded_by', 'industry', 'established')
    search_fields = ('company', 'employees', 'founded_by', 'industry', 'established')

    ordering = ('company', 'headquarters', 'founded_by', 'established')
    prepopulated_fields = {"website": ("company",)}


@admin.register(Employee)
class EmployeeFields(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'position','employee_picture', 'company')
    search_fields = ('first_name', 'last_name', 'email')  # Add search functionality
    list_filter = ('position', 'company')
    ordering = ('first_name', 'last_name')


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch_type', 'branch_image', 'manager_name', 'company', 'phone_number', 'email', 'opened_on')
    search_fields = ('name', 'manager_name', 'company__name', 'email','branch_type')
    list_filter = ( 'opened_on', 'company','branch_type', 'location')

    # Allow inline editing of image field and other fields
    ordering = ('-opened_on',)


class CompanyAdmin(admin.AdminSite):
    site_header = 'Companies Admin'
    site_title = site_header
    index_title = 'Companies Management'

company_admin = CompanyAdmin(name='company-admin')
company_admin.register(Company, CompanyFields)
company_admin.register(CompanyInfo, CompanyInfoFields)
company_admin.register(Employee, EmployeeFields)
company_admin.register(Branch, BranchAdmin)


