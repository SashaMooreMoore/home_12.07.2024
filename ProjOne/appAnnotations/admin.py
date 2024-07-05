from django.contrib import admin
from .models import Info, Bank

@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'balance']
    list_display_links = ['id', 'title', 'balance']


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'percent', 'balance']
    list_display_links = ['first_name', 'percent', 'balance']