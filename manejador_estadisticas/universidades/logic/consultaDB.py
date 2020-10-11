from manejador_busquedas.models import Consulta
from manejador_usuarios.models import Estudiante
from manejador_contenido.models import Proveedor
from django.db.models import Count


def get_Consultas():

    consultas = Consulta.objects.all()

    return consultas


def get_proveedores_por_carrerra(p_carrera, p_universidad):

    # consultas = Proveedor.objects.filter(
    #     contenido__consulta__estudiante__carrera='Ingeniería de Sistemas')
    # consultas = Estudiante.objects.filter(
    #    consulta__contenido__proveedor_id__nombre='IEEE')
    #consultas = Estudiante.objects.values('carrera').filter(consulta__contenido__proveedor_id__nombre='IEEE')
    proveedores = Proveedor.objects.values('nombre').filter(
        contenido__consulta__estudiante__carrera=p_carrera, contenido__consulta__estudiante__universidad__nombre=p_universidad)

    print(proveedores)
    return proveedores


def get_carreras_universidad(p_universidad):
    carreras = Estudiante.objects.values('carrera').filter(
        universidad__nombre=p_universidad)
    print(carreras)
    return carreras
