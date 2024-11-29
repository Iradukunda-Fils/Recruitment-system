from django.contrib import admin
from .models import Notification

# Register your models here.

@admin.register(Notification)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'message', 'timestamp', 'is_read', )
    list_filter = ('timestamp', 'recipient', 'is_read')
    search_fields = ('timestamp', 'recipient', 'is_read')
    ordering = ('-timestamp',)

class CustomUserAdmin(admin.AdminSite):
    # The fields to be used in displaying the User model.
    pass
    
