
from booklick.models import Valor, Estadistica, ValorTipo2

def get_valores_estadistica(p_estadistica):
    valores = Valor.objects.filter(
        estadistica=p_estadistica).values_list('atributo', 'valor')
    return valores

def get_valores_tipo2_estadistica(p_estadistica):
    valores = ValorTipo2.objects.filter(
        estadistica=p_estadistica).values_list('atributo_carrera', 'atributo_proveedor', 'valor')
    return valores

def get_estadistica_reciente(p_estadistica):
    estadisticas = Estadistica.objects.filter(nombre=p_estadistica).order_by(
        '-fecha').values_list('id', 'fecha')
    estadistica = {'id': estadisticas[0][0],
                   'fecha': str(estadisticas[0][1])}
    # print(estadistica)
    return estadistica
