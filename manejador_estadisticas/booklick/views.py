from django.shortcuts import render
from django.http import HttpResponse
from manejador_contenido.models import Booklist
from manejador_usuarios.models import Estudiante
from django.core import serializers
import csv
import time

from .logic.booklick_logic import get_valores_estadistica, get_estadistica_reciente,get_estudiantes_por_carrerra,get_carreras,get_booklists_estudiante

from .logic.booklists_carrera import get_all_booklists
from email._header_value_parser import ContentDisposition
from collections import Counter
from . models import Estadistica, Valor, Tipo_estadistica


def get_booklists_carrera(request):
    carreras = get_carreras()
    
    response = HttpResponse(content_type='text/csv')
    
    writer = csv.writer(response)
     
    writer.writerow(['Carrera', 'NumBooklists'])


    booklistscarrera = [] 
    total = 0
    
    for carrera in carreras:
        booklists = 0
        carrera_act = carrera['carrera']
        estudiantes = get_estudiantes_por_carrerra(carrera_act)
        for estudiante in estudiantes:
            est_act = estudiante['codigo']
            booklists += get_booklists_estudiante(est_act)
        booklistscarrera.append((carrera_act,booklists))
        total += booklists
    nuevalista=sorted(booklistscarrera,key=lambda x:int(x[1]),reverse=True)
    for tupla in nuevalista:
        writer.writerow(tupla)
    writer.writerow(['TOTAL', total])

    response['Content-Disposition']= 'attachment; filename="booklistsCarrera.csv"'
        
    return response


def get_booklists_contenidoPromedio(request):

    booklists = get_all_booklists()
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)

    writer.writerow(['Promedio contenido Booklist:'])

    contador = 0
    total = 0
    num = 0

    for booklist in booklists:
        num = booklist.contenidos.all().count()+booklist.booklistsContenidos.all().count()
        total = total + num
        contador = contador + 1

    promedio = total/contador

    writer.writerow([promedio])
#
    response['Content-Disposition'] = 'attachment; filename="booklistsPromedioContenido.csv"'
#
    #respuesta = "La cantidad promedio de contenido en los Booklist es: " + str(promedio)

    return response

# Create your views here.


def contar(request):
    booklists = get_all_booklists()
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['0', '1-3', '5-10', 'Mas de 10'])
    cero = 0
    unoatres = 0
    cincoadiez = 0
    masdediez = 0
    for booklist in booklists:
        tamaño = booklist.contenidos.all().count(
        ) + booklist.booklistsContenidos.all().count()
        if tamaño == 0:
            cero += 1
        if 1 <= tamaño <= 3:
            unoatres += 1
        if 5 <= tamaño <= 10:
            cincoadiez += 1
        if tamaño > 10:
            masdediez += 1
    writer.writerow([cero, unoatres, cincoadiez, masdediez])
    response['Content-Disposition'] = 'attachment; filename="contenidoxbooklist.csv"'
    return response


def post_booklists_contenidoPromedio_db(request):

    booklists = get_all_booklists()
    response = HttpResponse(content_type='text/csv')
    contador = 0
    total = 0
    num = 0

    for booklist in booklists:
        num = booklist.contenidos.all().count()+booklist.booklistsContenidos.all().count()
        total = total + num
        contador = contador + 1

    promedio = total/contador

    estadistica = Estadistica.objects.create(
        nombre=Tipo_estadistica.BOOKLIST_PROMEDIO)
    valor = Valor.objects.create(
        atributo='promedio', valor=promedio, estadistica=estadistica)

    return HttpResponse('Exitoso')


def get_booklists_contenidoPromedio_db(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Promedio contenido Booklist:'])

    estadistica = get_estadistica_reciente(Tipo_estadistica.BOOKLIST_PROMEDIO)
    valores = get_valores_estadistica(estadistica.get('id'))
    promedio = str(valores[0]).split()[1]

    writer.writerow([promedio])
    fecha = 'Estadística calculada en:' + estadistica.get('fecha')
    writer.writerow([fecha])
    response['Content-Disposition'] = 'attachment; filename="booklistsPromedioContenido.csv"'

    return response


def post_booklists_carrera_db(request):
    
    carreras = get_carreras()
    
    estadistica = Estadistica.objects.create(
        nombre=Tipo_estadistica.BOOKLIST_CARRERA)

    for carrera in carreras:
        booklists = 0
        carrera_act = carrera['carrera']
        estudiantes = get_estudiantes_por_carrerra(carrera_act)
        for estudiante in estudiantes:
            est_act = estudiante['codigo']
            booklists += get_booklists_estudiante(est_act)
        
        valor = Valor.objects.create(
        atributo=carrera_act, valor=booklists, estadistica=estadistica)
        
    return HttpResponse('Exitoso')


def get_booklists_carrera_db(request):
    
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Carrera', 'NumBooklists'])

    estadistica = get_estadistica_reciente(Tipo_estadistica.BOOKLIST_CARRERA)
    valores = get_valores_estadistica(estadistica.get('id'))
   
    for tupla in valores:
        print(tupla)
        writer.writerow([tupla])

    response['Content-Disposition']= 'attachment; filename="booklistsCarrera.csv"'
        
    return response