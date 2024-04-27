from django.contrib import admin
from .models import Customer, Product

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        # Restrict access to view Customer model based on user role
        if request.user.is_superuser:
            return True  # Allow superusers to view Customer model
        return False  # Deny access to other users

    def has_change_permission(self, request, obj=None):
        # Restrict access to change Customer model based on user role
        if request.user.is_superuser:
            return True  # Allow superusers to change Customer model
        return False  # Deny access to other users
