# type: ignore
# flake8: noqa

from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'category', 'callsign', 'first_name', 'show',
    ordering = 'id',
    list_filter = 'category',
    search_fields = 'first_name', 'last_name', 'id', 'saram',
    list_per_page = 20
    list_max_show_all = 100
    # list_editable = 'first_name', 'last_name', 'phone'
    list_display_links = 'id',
    list_editable = 'callsign', 'show'


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'id',
