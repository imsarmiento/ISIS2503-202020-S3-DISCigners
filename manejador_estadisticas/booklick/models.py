from django.db import models
from usuarios.models import Estudiante
from django.contrib.postgres.fields import ArrayField


class Track(models.Model):
    nombre = models.CharField(max_length=50)
    lista_actividad = ArrayField(ArrayField(models.IntegerField()))
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s' % (self.nombre, self.lista_actividad, self.estudiante)
