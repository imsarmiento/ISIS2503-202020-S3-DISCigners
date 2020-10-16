from django.db import models
from datetime import datetime


class Tipo_estadistica(models.TextChoices):
    BOOKLIST_RANGO = 'BR', 'Booklist por rango'
    BOOKLIST_PROMEDIO = 'BP', 'Booklist promedio'
    BOOKLIST_CARRERA = 'BC', 'Booklist por carrera'

# Modelo de Proveedor


class Estadistica(models.Model):
    nombre = models.CharField(
        max_length=2, choices=Tipo_estadistica.choices)
    fecha = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return '%s %s' % (self.nombre, self.fecha)


class Valor(models.Model):
    atributo = models.CharField(max_length=50)
    valor = models.FloatField()
    estadistica = models.ForeingKey(Estadistica, on_delete=models.CASCADE))

    def __str__(self):
        return '%s %s' % (self.atributo, self.valor)
# Modelo de Contenido
