from django.db import models


class InsuranceProvider(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Facility(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    website = models.URLField(blank=True)
    insurance_accepted = models.ManyToManyField(
        InsuranceProvider,
        related_name='facilities',
        blank=True,
    )
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'facilities'
        ordering = ['state', 'city', 'name']

    def __str__(self):
        return f"{self.name} — {self.city}, {self.state}"
