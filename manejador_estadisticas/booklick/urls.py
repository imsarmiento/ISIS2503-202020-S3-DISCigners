from django.urls import path
from . import views

urlpatterns = [
    path('booklistsCarrera/', views.get_booklists_carrera, name='booklistsCarrera'),
    path('booklistsPromedioContenido/', views.get_booklists_contenidoPromedio,
         name='booklistsPromedioContenido'),
    path('booklistsCuantoContenido/', views.contar, name='booklistsContar'),
    path('booklistsPromedioContenido_db_post/', views.post_booklists_contenidoPromedio_db,
         name="booklistsPromedioContenido_db_post"),
    path('booklistsPromedioContenido_db_get/', views.get_booklists_contenidoPromedio_db,
         name="booklistsPromedioContenido_db_get"),
<<<<<<< HEAD
     path('booklistsCarrera_db_post/', views.post_booklists_carrera_db,
         name="booklistsCarrera_db_post"),
    path('booklistsCarrera_db_get/', views.get_booklists_carrera_db,
         name="booklistsCarrera_db_get"),
=======
    path('booklistsRango_db_post/', views.post_booklists_rangos_db,
         name="booklistsRangos_db_post"),
    path('booklistsRango_db_get/', views.get_booklists_rangos_db,
         name="booklistsRangos_db_get"),
>>>>>>> e2eaea0110f6ad3dfc65901a1f7647789030c7d0
]
