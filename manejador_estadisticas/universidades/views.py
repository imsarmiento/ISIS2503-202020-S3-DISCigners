from django.shortcuts import render
from django.http import HttpResponse
from .logic.consultaDB import get_consultas_universidad, get_proveedores_por_carrerra, get_carreras_universidad
from manejador_contenido.models import Contenido
from manejador_contenido.logic.logic_contenido import get_contenido
from manejador_usuarios.logic.logic_usuarios import get_estudiantes
from django.core import serializers
from collections import Counter
import csv
import time


"""
Genera archivo con las bases de datos más consultadas (numConsultas)
Ejemplo: http://localhost:8000/universidades/basesDatos/Uniandes/2020-01-01/2021-10-10
"""


def get_basesDatos(request, universidad, fechaInicio, fechaFin):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Universidad', universidad])
    writer.writerow(['Fechas', fechaInicio + " / " + fechaFin])
    writer.writerow(['Proveedor', 'NumeroConsultas'])

    arreglo = []
    frecuencia = []
    diferentes = []
    for consulta in get_consultas_universidad(universidad, fechaInicio, fechaFin).values_list('estudiante', 'contenido', 'fecha'):
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
        actual = diferentes[i] + ';' + str(frecuencia[i])
        lista.append(tuple(map(str, actual.split(';'))))
        i += 1
    nuevaLista = sorted(lista, key=lambda x: int(x[1]), reverse=True)

    for tupla in nuevaLista:
        writer.writerow(tupla)

    response['Content-Disposition'] = 'attachment; filename="DB_Consultadas.csv"'

    return response


"""
Genera archivo con estadisticas sobre el número de consultas a una base de datos por carrera
Necesita la universidad y las fechas en las que se quiere incluir el reporte
Ej. http://localhost:8000/universidades/basesDatos_carreras/Universidad%20de%20los%20Andes/2020-01-01/2021-10-10
"""


def get_basesDatos_carrera(request, universidad, fechaInicio, fechaFin):
    startO = time.time()
    consulta = 0
    calculos = 0
    write = 0
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Universidad', universidad])
    writer.writerow(['Fechas', fechaInicio + " / " + fechaFin])

    writer.writerow(['Proveedor', 'NumeroConsultas'])

    start = time.time()
    carreras_tot = get_carreras_universidad(universidad)
    now = time.time()
    consulta += (now-start)
    start = time.time()
    carreras = []
    for i in range(len(carreras_tot)):
        carrera_act = carreras_tot[i]
        carreras.append(carrera_act['carrera'])
    # print(carreras)
    now = time.time()
    calculos += (now-start)
    estadisticas = []
    for carrera in carreras:

        writer.writerow(['Carrera', carrera])
        start = time.time()
        proveedores = get_proveedores_por_carrerra(
            carrera, universidad, fechaInicio, fechaFin)
        consulta += (now-start)
        start = time.time()
        lista_carrera = {}
        for proveedor_dict in proveedores:
            proveedor = proveedor_dict['nombre']
            if not lista_carrera.get(proveedor, False):
                lista_carrera.update({proveedor: 1})
            else:
                lista_carrera[proveedor] += 1
        # print(lista_carrera)
        sort_proveedores = sorted(
            lista_carrera.items(), key=lambda x: x[1], reverse=True)
        # print(sort_proveedores)
        now = time.time()
        calculos += (now-start)
        start = time.time()
        for proveedor in sort_proveedores:
            writer.writerow(proveedor)

        writer.writerow(['', ''])
        now = time.time()
        write += (now-start)

    response['Content-Disposition'] = 'attachment; filename="DB_Consultadas_Por_Carrera.csv"'
    endO = time.time()
    tiempoTot = endO-startO
    print('Consulta: '+str(consulta))
    print('Calculos: '+str(calculos))
    print('Write: '+str(write))
    print('Tot: '+str(tiempoTot))
    return response
