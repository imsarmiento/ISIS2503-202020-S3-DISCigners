from django.urls import path
from . import views

urlpatterns = [
        path('booklistscarrera/', views.get_booklists, name='booklistsCarrera')
    ]