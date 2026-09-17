from django.db import models
from django.conf import settings


class Diagnosis(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    body_region = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'diagnoses'
        ordering = ['body_region', 'name']

    def __str__(self):
        return self.name


class PatientProfile(models.Model):
    PT_STATUS_CHOICES = [
        ('not_started', 'Have not started PT'),
        ('currently_in', 'Currently in PT'),
        ('completed', 'Completed PT'),
        ('planning', 'Planning to start PT'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    diagnosis = models.ForeignKey(
        Diagnosis,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    pt_status = models.CharField(
        max_length=20,
        choices=PT_STATUS_CHOICES,
        default='not_started',
    )
    current_facility = models.CharField(max_length=200, blank=True)
    had_surgery = models.BooleanField(default=False)
    surgery_date = models.DateField(null=True, blank=True)
    pain_level = models.IntegerField(default=5)
    questionnaire_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
