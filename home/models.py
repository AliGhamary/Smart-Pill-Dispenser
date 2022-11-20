from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Pill(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    hour = models.IntegerField( null=True, blank=True,
    validators=[
            MaxValueValidator(23),
            MinValueValidator(0)
        ]
    )
    minute = models.IntegerField( null=True, blank=True,
    validators=[
            MaxValueValidator(59),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return self.name or 'None'