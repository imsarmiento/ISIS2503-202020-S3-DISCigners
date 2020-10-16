from ..models import Valor, Estadistica
from datetime import datetime


def get_valores_estadistica(p_estadistica):
    valores = Valor.objects.filter(
        estadistica=p_estadistica)
    print(valores)
    return valores


def get_estadistica_reciente(p_estadistica):
    estadisticas = Estadistica.objects.order_by(
        '-fecha').values_list('id', 'fecha')
    estadistica = {'id': estadisticas[0][0],
                   'fecha': str(estadisticas[0][1])}
    print(estadistica)
    return estadistica
