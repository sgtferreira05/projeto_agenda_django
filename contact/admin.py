from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'saram', 'phone', 'created_date',
    ordering = 'id',
    # list_filter = 'created_date',
    search_fields = 'first_name', 'last_name', 'id', 'saram',
    list_per_page = 20
    list_max_show_all = 100
    # list_editable = 'first_name', 'last_name', 'phone'
