from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    apellido=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    
    def __str__(self):
        return f'Usuario {self.id}: {self.nombre} {self.apellido} {self.email}'
