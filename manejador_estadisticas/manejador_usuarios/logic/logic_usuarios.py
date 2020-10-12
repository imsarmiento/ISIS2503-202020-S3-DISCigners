from ..models import Estudiante


def get_estudiantes():

    estudiantes = Estudiante.objects.all()

    return estudiantes
