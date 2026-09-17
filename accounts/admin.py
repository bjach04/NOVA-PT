from django.contrib import admin
from .models import Diagnosis, PatientProfile


@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ['name', 'body_region', 'slug']
    list_filter = ['body_region']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'diagnosis', 'pt_status', 'pain_level', 'questionnaire_completed']
    list_filter = ['pt_status', 'had_surgery', 'questionnaire_completed', 'diagnosis']
    search_fields = ['user__username', 'user__email']
    raw_id_fields = ['user']
