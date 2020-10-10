from manejador_busquedas.models import Consulta
from django.db.models import Count


def get_Consultas():

    consultas = Consulta.objects.all()

    return consultas
