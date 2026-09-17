from django.contrib import admin
from .models import InsuranceProvider, Facility


@admin.register(InsuranceProvider)
class InsuranceProviderAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'state', 'zip_code', 'phone']
    list_filter = ['state', 'insurance_accepted']
    search_fields = ['name', 'city', 'zip_code']
    filter_horizontal = ['insurance_accepted']
