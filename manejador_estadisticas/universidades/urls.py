from django.urls import path
from . import views

urlpatterns = [
    path('basesDatos/<str:universidad>/<str:fechaInicio>/<str:fechaFin>', views.get_basesDatos, name='basesDatos'),
    path('basesDatos_carreras/<str:universidad>/<str:fechaInicio>/<str:fechaFin>', views.get_basesDatos_carrera,
         name='basesDatos_carrera')
]
