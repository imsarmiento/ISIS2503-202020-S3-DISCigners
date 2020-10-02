from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    descripcion = models.TextField()
    intereses = models.TextField()

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)


class Actividad(models.Model):
    idActividad = models.IntegerField()
    fecha = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s' % (self.idActividad, self.fecha, self.usuario)
