from django.db import models
from django.utils import timezone

# Create your models here.

class usuario(models.Model):
    name = models.CharField(max_length=15, unique=True)
    rol = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.name
