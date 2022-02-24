from django.db import models
from django.utils import timezone

class Smoothie(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)
    ingredients = models.TextField()


    def __str__(self):
        return f"Smoothie {self.name}"
