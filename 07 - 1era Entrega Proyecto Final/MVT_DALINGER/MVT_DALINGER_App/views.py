from tkinter.font import families
from django.shortcuts import render

# Create your views here.

#Importamos lo necesario proyecto:
from django.http import HttpResponse
from django.template import loader

from MVT_DALINGER_App.models import Familiar

def nuevo_familiar(request):
    familiar_1 = Familiar(nombre="fede", edad=28, fecha_alta="1993-11-6")
    familiar_1.save()
    familiar_2 = Familiar(nombre="jony", edad=28, fecha_alta="1993-11-6")
    familiar_2.save()
    familiar_3 = Familiar(nombre="maxi", edad=28, fecha_alta="1993-11-6")
    familiar_3.save()

    familiares = [familiar_1, familiar_2, familiar_3] 
    diccionario = {"familiares":familiares}

    plantilla = loader.get_template("template_1.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)
    
###################### Agregado de Playground Intermedio Parte 1 ########################

def inicio (request):
    # return HttpResponse("Pagina de inicio")
    return render (request, "MVT_DALINGER_App/inicio.html")
    # Para el uso de contexto:
    # return render (request, "MVT_DALINGER_App/inicio.html", contexto)

def curso (request):
    # return HttpResponse("Pagina de cursos")
    return render (request, "MVT_DALINGER_App/curso.html")

def profesores (request):
    # return HttpResponse("Pagina de profesores")
    return render (request, "MVT_DALINGER_App/profesores.html")

def estudiantes (request):
    # return HttpResponse("Pagina de estudiantes")
    return render (request, "MVT_DALINGER_App/estudiantes.html")

def entregables (request):
    # return HttpResponse("Pagina de entregables")
    return render (request, "MVT_DALINGER_App/entregables.html")