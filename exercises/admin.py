from django.contrib import admin
from .models import Exercise


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'diagnosis', 'phase', 'difficulty', 'pain_level_min', 'pain_level_max']
    list_filter = ['diagnosis', 'phase', 'difficulty']
    search_fields = ['title', 'description']
