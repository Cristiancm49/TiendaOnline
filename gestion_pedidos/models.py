from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(blank= True, null= True)
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre


class Articulos(models.Model):
    nombre = models.CharField(max_length=40)
    seccion = models.CharField(max_length=15)
    precio = models.IntegerField()

    def __str__(self):
        return 'El nombre es: %s la seccion es: %s y el precio es: %s' %(self.nombre, self.seccion, self.precio)

class Pedido(models.Model):
    numbero_pedido = models.IntegerField()
    fecha = models.DateField()
    estado = models.BooleanField()