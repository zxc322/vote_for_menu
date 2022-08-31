from django.contrib import admin

from .models import Menus


@admin.register(Menus)
class MenusAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "restaurant")
