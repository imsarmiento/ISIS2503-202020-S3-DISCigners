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
from django.contrib.auth.decorators import login_required
from manejador_estadisticas.auth0backend import getRole
from booklick.models import Estadistica, Valor, ValorTipo2, Tipo_estadistica
from .logic.estadisticas import get_valores_estadistica, get_valores_tipo2_estadistica, get_estadistica_reciente

"""
Genera archivo con las bases de datos más consultadas (numConsultas)
Ejemplo: http://localhost:8000/universidades/basesDatos/Uniandes/2020-01-01/2021-10-10
"""

def universidades(request):
    return render(request, 'Universidades/universidades.html')


@login_required
def post_basesDatos(request, universidad, fechaInicio, fechaFin):
    #role = getRole(request)
    #if role == "Administrador Universidad":
    estadistica = Estadistica.objects.create(
            nombre=Tipo_estadistica.UNIVERSIDAD_PROVEEDORES_P)
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
        valor = Valor.objects.create(
                atributo=tupla, valor=nuevaLista[tupla], estadistica=estadistica)
    return HttpResponse('Exitoso')
    
def get_viejo_basesDatos(request, universidad, fechaInicio, fechaFin):
    role = getRole(request)
    if role == "Administrador Universidad":
        response = HttpResponse(content_type='text/csv')

        writer = csv.writer(response)
        writer.writerow(['Universidad', universidad])
        writer.writerow(['Fechas', fechaInicio + " / " + fechaFin])
        writer.writerow(['Proveedor', 'NumeroConsultas'])
        
        estadistica = get_estadistica_reciente(Tipo_estadistica.UNIVERSIDAD_PROVEEDORES_P)
        valores = get_valores_estadistica(estadistica.get('id'))
        for tupla in valores:
            writer.writerow(tupla)

        response['Content-Disposition'] = 'attachment; filename="DB_Consultadas.csv"'

        return response
    else:
        #return HttpResponse("Unauthorized User")
        return render(request, 'Universidades/unuser.html')

def get_viejo_basesDatos(request, universidad, fechaInicio, fechaFin):
    role = getRole(request)
    if role == "Administrador Universidad":
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
    else:
        #return HttpResponse("Unauthorized User")
        return render(request, 'Universidades/unuser.html')







"""
Genera archivo con estadisticas sobre el número de consultas a una base de datos por carrera
Necesita la universidad y las fechas en las que se quiere incluir el reporte
Ej. http://localhost:8000/universidades/basesDatos_carreras/Universidad%20de%20los%20Andes/2020-01-01/2021-10-10
"""



def get_basesDatos_carrera(request, universidad, fechaInicio, fechaFin):
    startO = time.time()
    role = getRole(request)
    if role == "Administrador Universidad":
        consulta = 0
        calculos = 0
        write = 0
        response = HttpResponse(content_type='text/csv')

        writer = csv.writer(response)
        writer.writerow(['Universidad', universidad], " ")
        writer.writerow(['Fechas', fechaInicio + " / " + fechaFin], " ")

        writer.writerow(['Carrera','Proveedor', 'NumeroConsultas'])
        estadistica = get_estadistica_reciente(Tipo_estadistica.UNIVERSIDAD_PROVEEDORES_C)
        valores = get_valores_tipo2_estadistica(estadistica.get('id'))
        for valor in valores:
            writer.writerow(valor)
        response['Content-Disposition'] = 'attachment; filename="DB_Consultadas_Por_Carrera.csv"'
        return response
    else:
        #return HttpResponse("Unauthorized User")
        return render(request, 'Universidades/unuser.html')

def post_basesDatos_carrera(request, universidad, fechaInicio, fechaFin):
    #role = getRole(request)
    #if role == "Administrador Universidad":
    estadistica = Estadistica.objects.create(
        nombre=Tipo_estadistica.UNIVERSIDAD_PROVEEDORES_C)
    consulta = 0
    calculos = 0
    write = 0
    carreras_tot = get_carreras_universidad(universidad)
    carreras = []
    for i in range(len(carreras_tot)):
        carrera_act = carreras_tot[i]
        carreras.append(carrera_act['carrera'])
    estadisticas = []
    for carrera in carreras:
        writer.writerow(['Carrera', carrera])
        proveedores = get_proveedores_por_carrerra(
            carrera, universidad, fechaInicio, fechaFin)
        lista_carrera = {}
        for proveedor_dict in proveedores:
            proveedor = proveedor_dict['nombre']
            if not lista_carrera.get(proveedor, False):
                lista_carrera.update({proveedor: 1})
            else:
                lista_carrera[proveedor] += 1
        sort_proveedores = sorted(
            lista_carrera.items(), key=lambda x: x[1], reverse=True)
        for proveedor in sort_proveedores:
            valorTipo2 = ValorTipo2.objects.create(
            atributo_carrera=carrera, atributo_proveedor=proveedor, valor=sort_proveedores[proveedor], estadistica=estadistica)
    return HttpResponse('Exitoso')
    #else:
        #return HttpResponse("Unauthorized User")
    #    return render(request, 'Universidades/unuser.html')

def get_viejo_basesDatos_carrera(request, universidad, fechaInicio, fechaFin):
    if role == "Administrador Universidad":
        response = HttpResponse(content_type='text/csv')

        writer = csv.writer(response)
        writer.writerow(['Universidad', universidad])
        writer.writerow(['Fechas', fechaInicio + " / " + fechaFin])
        writer.writerow(['Proveedor', 'NumeroConsultas'])

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
    else:
        #return HttpResponse("Unauthorized User")
        return render(request, 'Universidades/unuser.html')
