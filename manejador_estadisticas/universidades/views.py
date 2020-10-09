from django.shortcuts import render
from django.http import HttpResponse
from .logic.consultaDB import get_Consultas
from manejador_contenido.models import Contenido
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
        proveedor =''
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
        lista.append(tuple(map(str,actual.split(','))))
        i += 1
    nuevaLista = sorted(lista, key = lambda x: x[1], reverse=True)

    for tupla in nuevaLista:
        writer.writerow(tupla)

    response['Content-Disposition'] = 'attachment; filename="DB_Consultadas.csv"'

    return response