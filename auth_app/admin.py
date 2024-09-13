from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserAuditLog

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'role', 'is_staff', 'is_active']
    list_filter = ['role', 'is_staff', 'is_active']
    search_fields = ['email']
    ordering = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'password', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'role', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(UserAuditLog)
class UserAuditLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'changed_by', 'timestamp')
    search_fields = ('user__email', 'changed_by__email')
    list_filter = ('action', 'timestamp')