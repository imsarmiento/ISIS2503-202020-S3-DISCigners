from ..models import Valor, Estadistica
from manejador_contenido.models import Booklist
from manejador_usuarios.models import Estudiante
from datetime import datetime


def get_valores_estadistica(p_estadistica):
    valores = Valor.objects.filter(
        estadistica=p_estadistica).values_list('atributo', 'valor')
    return valores


def get_estadistica_reciente(p_estadistica):
    estadisticas = Estadistica.objects.order_by(
        '-fecha').values_list('id', 'fecha')
    estadistica = {'id': estadisticas[0][0],
                   'fecha': str(estadisticas[0][1])}
    # print(estadistica)
    return estadistica

def get_estudiantes_por_carrerra(p_carrera):
    estudiantes = Estudiante.objects.values('codigo').filter(carrera=p_carrera)

    return estudiantes

def get_carreras():
    carreras = Estudiante.objects.values('carrera').distinct()
        
    return carreras

def get_booklists_estudiante(p_creador):
    booklists = Booklist.objects.filter(creador=p_creador).count()
        
    return booklists