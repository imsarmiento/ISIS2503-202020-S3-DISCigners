from django.urls import path
from . import views

urlpatterns = [
        path('booklistscarrera/', views.get_booklists, name='booklistsCarrera'),
        path('booklistsPromedioContenido/', views.get_booklists_contenidoPromedio, name='booklistsPromedioContenido'),
        path('booklistsCuantoContenido/', views.contar,name = 'booklistsContar')
    ]