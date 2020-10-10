from django.urls import path
from . import views

urlpatterns = [
    path('basesDatos/', views.get_basesDatos, name='basesDatos'),
    path('basesDatos_carreras/', views.get_basesDatos_carrera,
         name='basesDatos_carrera')
]
