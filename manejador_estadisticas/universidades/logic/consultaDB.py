from manejador_busquedas.models import Consulta

def get_Consultas():

    consultas = Consulta.objects.all()

    return consultas