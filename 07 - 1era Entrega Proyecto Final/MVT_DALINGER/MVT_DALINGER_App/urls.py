from django.urls import path
from .views import *

urlpatterns = [
    #path("cursos/", cursos), #esta ya venia de antes
    path("nuevo_familiar/", nuevo_familiar), #essta venia del desafio entregable 06
    # path("inicio/", inicio),
    path("", inicio, name="inicio"), #para que no falle
    path("curso/", curso, name="curso"),
    path("profesores/", profesores, name="profesores"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("entregables/", entregables, name="entregables"),
    path("nuevo_familiar_formulario/", nuevo_familiar_formulario, name="nuevo_familiar_formulario"),
    path("busqueda_edad/", busqueda_edad, name="busqueda_edad"),
    path("buscar/", buscar, name="buscar"),

]