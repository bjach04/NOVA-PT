from django.contrib import admin
from .models import FAQ


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'diagnosis', 'answered_by', 'featured']
    list_filter = ['featured', 'diagnosis']
    search_fields = ['question', 'answer']
