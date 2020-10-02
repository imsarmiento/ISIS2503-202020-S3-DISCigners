from usuarios.models import Actividad


def calcular_track(estudiantep):
    track = ""
    actividades = Actividad.objects.filter(estudiante=estudiantep)
    for actividad in actividades:
        track += actividad.idActividad + ", "
    return track

# revisar


def generar_track(estudiantep):
    lista = calcular_track(estudiantep)
    Actividad(nombre="Prueba", lista_actividad=lista, estudiante=estudiantep)
