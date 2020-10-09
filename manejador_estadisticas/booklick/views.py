from django.shortcuts import render
from django.http import HttpResponse
from manejador_contenido.models import Booklist
from manejador_usuarios.models import Estudiante
from django.core import serializers
import csv

from .logic.booklists_carrera import get_all_booklists
from email._header_value_parser import ContentDisposition
from collections import Counter

def get_booklists (request):
    
    booklists = get_all_booklists()
    response = HttpResponse(content_type='text/csv')
    
    writer = csv.writer(response)
     
    writer.writerow(['Carrera', 'NumBooklists'])
     
     
    arreglo = []
    frecuencua = []
    diferentes = []
    for booklist in booklists.values_list('titulo', 'creador', 'contenedor', 'contenidos'):
        carrera=''
        for estudiante in Estudiante.objects.all():
            if estudiante.get_codigo() == booklist[1]:
                carrera = estudiante.get_carrera()
                
        arreglo.append(carrera)
    diferentes = list(Counter(arreglo).keys())
    frecuencia = list(Counter(arreglo).values())
    
    i = 0
    lista = []
    while i < len(diferentes):
        actual=diferentes[i]+','+str(frecuencia[i])
        lista.append(tuple(map(str,actual.split(','))))
        i+=1
    nuevalista=sorted(lista,key=lambda x:x[1],reverse=True)
    
    for tupla in nuevalista:
        writer.writerow(tupla)
#     writer.writerow([booklist[0]+','+carrera])
#         
    response['Content-Disposition']= 'attachment; filename="booklistsxarrera.csv"'
#     
    return response

# Create your views here.
