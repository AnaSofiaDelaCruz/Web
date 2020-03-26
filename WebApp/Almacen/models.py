from django.db import models

# Create your models here.
class datosAlmacen(models.Model):
    nombreProducto = models.CharField(max_length = 250, null = False)
    fechaIngreso = models.CharField(max_length = 250, null = False)
    fechaCaducidad = models.CharField(max_length = 250, null = False)
    cantidad = models.CharField(max_length = 250, null = False)
    ventasPieza = models.CharField(max_length = 250, null = False)
