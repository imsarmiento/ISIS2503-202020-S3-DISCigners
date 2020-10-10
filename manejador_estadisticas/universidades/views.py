from django.shortcuts import render
from django.http import HttpResponse
from .logic.consultaDB import get_Consultas
from .logic.consultaDB import get_consultas_proveedor
from manejador_contenido.models import Contenido
from manejador_contenido.logic.logic_contenido import get_contenido
from manejador_usuarios.logic.logic_usuarios import get_estudiantes
from django.core import serializers
from collections import Counter
import csv


def get_basesDatos(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)

    writer.writerow(['Proveedor', 'NumeroConsultas'])
    arreglo = []
    frecuencia = []
    diferentes = []
    for consulta in get_Consultas().values_list('estudiante', 'contenido', 'fecha'):
        proveedor = ''
        for contenido in Contenido.objects.all():
            if contenido.get_Titulo() == consulta[1]:
                proveedor = contenido.get_proveedor()
        arreglo.append(proveedor)
    diferentes = list(Counter(arreglo).keys())
    frecuencia = list(Counter(arreglo).values())

    i = 0
    lista = []
    while i < len(diferentes):
        actual = diferentes[i] + ',' + str(frecuencia[i])
        lista.append(tuple(map(str, actual.split(','))))
        i += 1
    nuevaLista = sorted(lista, key=lambda x: x[1], reverse=True)

    for tupla in nuevaLista:
        writer.writerow(tupla)

    response['Content-Disposition'] = 'attachment; filename="DB_Consultadas.csv"'

    return response


def get_basesDatos_carrera(request):
    consultas = get_Consultas()
    #consulta_list = serializers.serialize('json', consultas)
    cotenidoTot = get_contenido()
    estudiantes = get_estudiantes()
    arreglo = []
    for consulta in consultas:
        proveedor = ''
        for contenido in cotenidoTot:
            if contenido.get_Titulo() == consulta[1]:
                proveedor = contenido.get_proveedor()
                break
        for estudiante in estudiantes:
            if estudiante.get_id() == consulta[2]:
                estudiante = consulta.get_estudiante()
                carrera = estudiante.get_carrera()
                break
        pareja = [proveedor, carrera]
        arreglo.append(pareja)

    return HttpResponse(consulta_list, content_type='application/json')
