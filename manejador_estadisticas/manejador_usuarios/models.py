from django.db import models
#from django.apps import apps
#Proveedor = apps.get_model('manejador_contenido', 'Proveedor')
#import manejador_contenido.models as Contenido
# Modelo de Universidad


class Universidad(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    #proveedores = models.ManyToManyField(Contenido.Proveedor)


# Modelo de Usuario
# Clase abstracta


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    descripcion = models.TextField()
    intereses = models.TextField()

    class Meta:
        abstract = True

    def _str_(self):
        return '%s %s' % (self.nombre, self.apellido)


# Modelo de Estudiante
# Instanciacion de usuario


class Estudiante(Usuario):
    carrera = models.CharField(max_length=50)
    codigo = models.IntegerField()
