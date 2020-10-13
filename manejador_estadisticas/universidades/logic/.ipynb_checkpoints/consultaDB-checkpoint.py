from manejador_busquedas.models import Consulta
from manejador_usuarios.models import Estudiante
from manejador_contenido.models import Proveedor
from django.db.models import Count


def get_consultas_universidad(p_universidad, fechaInicio, fechaFin):

    consultas = Consulta.objects.all().filter(
        estudiante__universidad__nombre=p_universidad,
        fecha__range=[fechaInicio, fechaFin])

    return consultas


def get_proveedores_por_carrerra(p_carrera, p_universidad, fechaInicio, fechaFin):
    proveedores = Proveedor.objects.values('nombre').filter(
        contenido__consulta__estudiante__carrera=p_carrera, contenido__consulta__estudiante__universidad__nombre=p_universidad, contenido__consulta__fecha__range=[fechaInicio, fechaFin])

    # print(proveedores)
    return proveedores


def get_carreras_universidad(p_universidad):
    carreras = Estudiante.objects.values('carrera').filter(
        universidad__nombre=p_universidad).distinct()
    # print("carreras")
    # print(carreras)
    return carreras
