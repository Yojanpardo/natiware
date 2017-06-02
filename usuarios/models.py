from django.db import models

# Create your models here.

class Usuario(models.Model):
    name = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)
    rol = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.name
