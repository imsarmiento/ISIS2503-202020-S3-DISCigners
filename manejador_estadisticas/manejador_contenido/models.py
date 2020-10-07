from django.db import models


class Tipo_conexion(models.TextChoices):
    API = 'AP', 'Api'
    METADATOS = 'MD', 'Metadatos'
    CORREO = 'CR', 'Correo'

# Modelo de Proveedor


class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    tipo_conexion = models.CharField(choices=Tipo_conexion.choices)


# Modelo de Contenido


class Contenido(models.Model):
    carrera = models.CharField(max_length=50)
    codigo = models.IntegerField()
