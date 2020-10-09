from django.db import models
#from django.apps import apps
#Estudiante = apps.get_model('manejador_usuarios', 'Estudiante')
import manejador_usuarios.models as Usuarios


class Tipo_conexion(models.TextChoices):
    API = 'AP', 'Api'
    METADATOS = 'MD', 'Metadatos'
    CORREO = 'CR', 'Correo'

# Modelo de Proveedor


class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    tipo_conexion = models.CharField(
        max_length=2, choices=Tipo_conexion.choices)
    universidaddes = models.ManyToManyField(Usuarios.Universidad)


# Modelo de Contenido

class Contenido(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=200)
    descripcion = models.TextField()


# Modelo Booklist


class Booklist(models.Model):
    titulo = models.CharField(max_length=50)
    creador = models.ForeignKey(Usuarios.Estudiante, on_delete=models.CASCADE)
    contenedor = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.SET_NULL)
    contenidos = models.ManyToManyField(Contenido)
    
    def get_creador(self):
        return creador;
