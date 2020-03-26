from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField(max_length = 250, null = False)
    apellido = models.CharField(max_length = 250, null = False)
    edad = models.IntegerField(max_length = 254, null = False)
