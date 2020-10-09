from django.shortcuts import render
from django.http import HttpResponse
from .logic.consultaDB import get_Consultas
from manejador_contenido.models import Contenido
import csv

def get_basesDatos(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)


    writer.writerow(['Contenido', 'Proveedor'])

    for consulta in get_Consultas().values_list('estudiante', 'contenido', 'fecha'):
        proveedor =''
        for contenido in Contenido.objects.all():
            if contenido.get_Titulo() == consulta[1]:
                proveedor = contenido.get_proveedor()
        writer.writerow([consulta[1]+','+proveedor])

    response['Content-Disposition'] = 'attachment; filename="DB_Consultadas.csv"'

    return response