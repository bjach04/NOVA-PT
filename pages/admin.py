from django.contrib import admin
from .models import MerchItem


@admin.register(MerchItem)
class MerchItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'active', 'created_at']
    list_filter = ['active']
    search_fields = ['name', 'description']
