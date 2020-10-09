from django.urls import path
from . import views

urlpatterns = [
    path('basesDatos/', views.get_basesDatos, name='basesDatos')
]