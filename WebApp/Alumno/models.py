from django.db import models

# Create your models here.
class materia(models.Model):
    nombre = models.CharField(max_length= 254, null = False)

class Alumno(models.Model):
    materia = models.ForeignKey(materia, on_delete = models.CASCADE)
    nombreAlumno = models.CharField(max_length= 254, null = False)
    carrera = models.CharField(max_length= 254, null = False)
    edad = models.IntegerField(null = False)
    direccion = models.CharField(max_length= 254, null = False)
    genero = models.CharField(max_length= 254, null = False)  
    matricula = models.CharField(max_length= 254, null = False)
