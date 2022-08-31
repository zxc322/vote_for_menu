from django.contrib import admin

from .models import ExtendedUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


class ExtendedUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Info'), {'fields': ('is_employee', 'is_restaurant_creator', 'voted_menu')}),
    )


admin.site.register(ExtendedUser, ExtendedUserAdmin)
