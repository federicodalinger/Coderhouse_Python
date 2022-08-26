from django.urls import path
from .views import *

urlpatterns = [
    #path("cursos/", cursos), #esta ya venia de antes
    path("nuevo_familiar/", nuevo_familiar), #essta venia del desafio entregable 06
    # path("inicio/", inicio),
    path("", inicio), #para que no falle
    path("curso/", curso),
    path("profesores/", profesores),
    path("estudiantes/", estudiantes),
    path("entregables/", entregables),

]