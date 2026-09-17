from django.db import models
from accounts.models import Diagnosis


class Exercise(models.Model):
    PHASE_CHOICES = [
        ('acute', 'Acute / Initial'),
        ('subacute', 'Sub-Acute'),
        ('strengthening', 'Strengthening'),
        ('advanced', 'Advanced / Return to Sport'),
        ('maintenance', 'Maintenance'),
    ]
    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    diagnosis = models.ForeignKey(
        Diagnosis,
        on_delete=models.CASCADE,
        related_name='exercises',
    )
    phase = models.CharField(max_length=20, choices=PHASE_CHOICES)
    pain_level_min = models.IntegerField(default=1)
    pain_level_max = models.IntegerField(default=10)
    sets = models.CharField(max_length=20, default='3')
    reps = models.CharField(max_length=50, default='10')
    video_url = models.URLField(blank=True)
    difficulty = models.CharField(
        max_length=15,
        choices=DIFFICULTY_CHOICES,
        default='beginner',
    )
    image = models.ImageField(upload_to='exercises/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['diagnosis', 'phase', 'difficulty']

    def __str__(self):
        return self.title
