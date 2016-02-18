from django.db import models
from django.utils import timezone

class Drink(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    mood = models.CharField(max_length=20)
    creator = models.ForeignKey('auth.User')
    published_date = models.DateTimeField(blank=True, null=True)
    def create(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.name

# Create your models here.
