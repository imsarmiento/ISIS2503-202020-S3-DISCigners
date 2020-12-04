from ..models import Contenido


def get_contenido():
    contenido = Contenido.objects.all()
    return contenido
