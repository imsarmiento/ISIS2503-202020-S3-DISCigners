from datetime import datetime
from django.db import models
import manejador_usuarios.models as Usuarios
import manejador_contenido.models as Contenidos

# Modelo de Consultas


class Consulta(models.Model):
    estudiante = models.ForeignKey(
        Usuarios.Estudiante, on_delete=models.CASCADE)
    contenido = models.ForeignKey(
        Contenidos.Contenido, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=datetime.now, blank=True)

    def get_estudiante(self):
        return self.estudiante.get_id()
# Create your models here.
