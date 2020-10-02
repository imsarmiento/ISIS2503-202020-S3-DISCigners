from django.db import models
from usuarios.models import Estudiante
from django.contrib.postgres.fields import ArrayField
from .logic import generarTrack


class Track(models.Model):
    nombre = models.CharField(max_length=50)
    lista_actividad = models.CharField(max_length=50)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    #lista_prueba = generarTrack.calcularTrack(estudiante)

    def __str__(self):
        return '%s %s %s' % (self.nombre, self.lista_actividad, self.estudiante)
