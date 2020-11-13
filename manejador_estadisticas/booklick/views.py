from django.shortcuts import render
from django.http import HttpResponse
from manejador_contenido.models import Booklist
from manejador_usuarios.models import Estudiante
from django.core import serializers
import csv
import time
from django.contrib.auth.decorators import login_required
from manejador_estadisticas.auth0backend import getRole


from .logic.booklick_logic import get_valores_estadistica, get_estadistica_reciente, get_estudiantes_por_carrerra, get_carreras, get_booklists_estudiante

from .logic.booklists_carrera import get_all_booklists
from email._header_value_parser import ContentDisposition
from collections import Counter
from . models import Estadistica, Valor, Tipo_estadistica

def booklist(request):
    return render(request, 'booklist.html')

@login_required
def get_booklists_carrera(request):
    role = getRole(request)
    if role == "Administrador Booklick":
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
            booklistscarrera.append((carrera_act, booklists))
            total += booklists
        nuevalista = sorted(
            booklistscarrera, key=lambda x: int(x[1]), reverse=True)
        for tupla in nuevalista:
            writer.writerow(tupla)
        writer.writerow(['TOTAL', total])

        response['Content-Disposition'] = 'attachment; filename="booklistsCarrera.csv"'

        return response
    else:
        return HttpResponse("Unauthorized User")

@login_required
def get_booklists(request):
    role = getRole(request)
    if role == "Administrador Booklick":
        booklists = get_all_booklists()
        response = HttpResponse(content_type='text/csv')

        writer = csv.writer(response)

        writer.writerow(['Carrera', 'NumBooklists'])

        arreglo = []
        frecuencua = []
        diferentes = []
        start = time.time()
        booklists = booklists.values_list(
            'titulo', 'creador', 'booklistsContenidos', 'contenidos')
        # now = time.time()
        # consulta = now-start

        # start = time.time()
        for booklist in booklists:
            carrera = ''
            for estudiante in Estudiante.objects.all():
                if estudiante.get_codigo() == booklist[1]:
                    carrera = estudiante.get_carrera()

            arreglo.append(carrera)
        diferentes = list(Counter(arreglo).keys())
        frecuencia = list(Counter(arreglo).values())

        i = 0
        lista = []
        while i < len(diferentes):
            actual = diferentes[i] + ',' + str(frecuencia[i])
            lista.append(tuple(map(str, actual.split(','))))
            i += 1
        # nuevalista=sorted(lista,key=lambda x:x[1],reverse=True)
        nuevalista = sorted(lista, key=lambda x: int(x[1]), reverse=True)
        now = time.time()
        calculos = now - start

        # print('Consulta: '+str(consulta))
        # print('Calculos: '+str(calculos))

        for tupla in nuevalista:
            writer.writerow(tupla)
        #     writer.writerow([booklist[0]+','+carrera])
        #
        response['Content-Disposition'] = 'attachment; filename="booklistsxarrera.csv"'
        #
        return response
    else:
        return HttpResponse("Unauthorized User")

@login_required
def get_booklists_contenidoPromedio(request):
    role = getRole(request)
    if role == "Administrador Booklick":
        booklists = get_all_booklists()
        response = HttpResponse(content_type='text/csv')

        writer = csv.writer(response)

        writer.writerow(['Promedio contenido Booklist:'])

        contador = 0
        total = 0
        num = 0

        for booklist in booklists:
            num = booklist.contenidos.all().count() + booklist.booklistsContenidos.all().count()
            total = total + num
            contador = contador + 1

        promedio = total / contador

        writer.writerow([promedio])
        #
        response['Content-Disposition'] = 'attachment; filename="booklistsPromedioContenido.csv"'
        #
        # respuesta = "La cantidad promedio de contenido en los Booklist es: " + str(promedio)

        return response
    
    else:
        return HttpResponse("Unauthorized User")


def contar(request):
    booklists = get_all_booklists()
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Contenido Booklists', '0', '1-3', '5-10', 'Mas de 10'])
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
    writer.writerow(['Cantidad', cero, unoatres, cincoadiez, masdediez])
    response['Content-Disposition'] = 'attachment; filename="contenidoxbooklist.csv"'
    return response


def post_booklists_contenidoPromedio_db(request):
    role = getRole(request)
    if role == "Administrador Booklick":
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
    role = getRole(request)
    if role == "Administrador Booklick":
        response = HttpResponse(content_type='text/csv')
        writer = csv.writer(response)
        writer.writerow(['Promedio contenido Booklist:'])

        estadistica = get_estadistica_reciente(Tipo_estadistica.BOOKLIST_PROMEDIO)
        print(estadistica)
        valores = get_valores_estadistica(estadistica.get('id'))
        print(valores)
        promedio = valores[0][1]
        writer.writerow([promedio])
        fecha = 'Estadística calculada en:' + estadistica.get('fecha')
        writer.writerow([fecha])
        response['Content-Disposition'] = 'attachment; filename="booklistsPromedioContenido.csv"'

        return response


def post_booklists_rangos_db(request):
    role = getRole(request)
    if role == "Administrador Booklick":
        booklists = get_all_booklists()
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

        estadistica = Estadistica.objects.create(
            nombre=Tipo_estadistica.BOOKLIST_RANGO)
        valor = Valor.objects.create(
            atributo='0', valor=cero, estadistica=estadistica)
        valor = Valor.objects.create(
            atributo='1-3', valor=unoatres, estadistica=estadistica)
        valor = Valor.objects.create(
            atributo='5-10', valor=cincoadiez, estadistica=estadistica)
        valor = Valor.objects.create(
            atributo='Mas de 10', valor=masdediez, estadistica=estadistica)
        return HttpResponse('Exitoso')


def get_booklists_rangos_db(request):
    role = getRole(request)
    if role == "Administrador Booklick":
        response = HttpResponse(content_type='text/csv')
        writer = csv.writer(response)
        writer.writerow(['Contenido Booklists', '0', '1-3', '5-10', 'Mas de 10'])
        estadistica = get_estadistica_reciente(Tipo_estadistica.BOOKLIST_RANGO)
        print(estadistica)
        valores = get_valores_estadistica(estadistica.get('id'))
        print(valores)    # print(valores)
        cero = 0
        unoatres = 0
        cincoadiez = 0
        masdediez = 0
        for i in range(len(valores)):
            atributo = valores[i][0]
            if atributo == '0':
                cero = valores[i][1]
            elif atributo == '1-3':
                unoatres = valores[i][1]
            elif atributo == '5-10':
                cincoadiez = valores[i][1]
            else:
                masdediez = valores[i][1]
        writer.writerow(['Cantidad', cero, unoatres, cincoadiez, masdediez])
        fecha = 'Estadística calculada en:' + estadistica.get('fecha')
        writer.writerow([fecha])
        response['Content-Disposition'] = 'attachment; filename="contenidoxbooklist.csv"'
        return response


def post_booklists_carrera_db(request):
    role = getRole(request)
    if role == "Administrador Booklick":
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
    role = getRole(request)
    if role == "Administrador Booklick":
        response = HttpResponse(content_type='text/csv')
        writer = csv.writer(response)
        writer.writerow(['Carrera', 'NumBooklists'])

        estadistica = get_estadistica_reciente(Tipo_estadistica.BOOKLIST_CARRERA)
        print(estadistica)
        valores = get_valores_estadistica(estadistica.get('id'))
        print(valores)
        for tupla in valores:
            writer.writerow(tupla)

        response['Content-Disposition'] = 'attachment; filename="booklistsCarrera.csv"'

        return response
