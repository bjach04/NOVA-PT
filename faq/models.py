from django.db import models
from accounts.models import Diagnosis


class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    diagnosis = models.ForeignKey(
        Diagnosis,
        on_delete=models.CASCADE,
        related_name='faqs',
        null=True,
        blank=True,
    )
    answered_by = models.CharField(max_length=200, help_text='Name and credentials, e.g. "Dr. Smith, DPT"')
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
        ordering = ['-featured', '-created_at']

    def __str__(self):
        return self.question
