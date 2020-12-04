from django.urls import path
from . import views

urlpatterns = [
    path('basesDatos_dp_get/<str:universidad>/<str:fechaInicio>/<str:fechaFin>', views.get_basesDatos, name='basesDatos'),
    path('basesDatos_dp_post/<str:universidad>/<str:fechaInicio>/<str:fechaFin>', views.post_basesDatos, name='basesDatos'),
    path('basesDatos_carreras_db_get/<str:universidad>/<str:fechaInicio>/<str:fechaFin>', views.get_basesDatos_carrera, name='basesDatos_carrera'), 
    path('basesDatos_carreras_db_post/<str:universidad>/<str:fechaInicio>/<str:fechaFin>', views.post_basesDatos_carrera,
         name='basesDatos_carrera'),    
    path('universidades/', views.universidades, name="universidadesGeneral")
]
