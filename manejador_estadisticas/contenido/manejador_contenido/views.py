from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .logic.logic_contenido import get_contenido


def print_contenido(request):
    contenido = get_contenido()
    contenido_list = serializers.serialize('json', contenido)
    return HttpResponse(contenido_list, content_type='application/json')

# Create your views here.
