from tkinter.font import families
from django.shortcuts import render

# Create your views here.

#Importamos lo necesario proyecto:
from django.http import HttpResponse
from django.template import loader

from MVT_DALINGER_App.models import Familiar
from MVT_DALINGER_App.forms import Familiar_formulario

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

''' VIEW PARA FORMULARIO A MANO:
    
    def nuevo_familiar_formulario(request):

    if request.method=="POST":
        nombre=request.POST.get("nombre")
        edad=request.POST.get("edad")
        fecha_alta=request.POST.get("fecha_alta")
        familiar=Familiar(nombre=nombre, edad=edad, fecha_alta=fecha_alta)
        familiar.save()
        return render(request, "MVT_DALINGER_App/inicio.html")
    return render(request, "MVT_DALINGER_App/nuevo_familiar_formulario.html")'''

def nuevo_familiar_formulario(request):

    if request.method=="POST":
        formulario_familiar = Familiar_formulario(request.POST)
        if formulario_familiar.is_valid():
            info= formulario_familiar.cleaned_data
            nombre= info["nombre"]
            edad= info["edad"]
            fecha_alta= info["fecha_alta"]
            familiar=Familiar(nombre=nombre, edad=edad, fecha_alta=fecha_alta)
            familiar.save()
            return render(request, "MVT_DALINGER_App/inicio.html", {"mensaje": "Familiar creado"})
        else:
            return render(request, "MVT_DALINGER_App/inicio.html", {"mensaje": "Error"})
    else:
        formulario_familiar = Familiar_formulario()
        return render(request, "MVT_DALINGER_App/nuevo_familiar_formulario.html", {"formulario": formulario_familiar})


def busqueda_edad(request):
    return render(request, "MVT_DALINGER_App/busqueda_edad.html")

def buscar(request):
    if request.GET["nombre"]:
        #nombrecito=request.GET.get("nombre") #es lo mismo que abajo.
        nombrecito=request.GET["nombre"] #GET es un diccionario, entonces puedo hacerlo asi.
        # return HttpResponse(f"buscamos el nombre: {nombrecito}")

        personas=Familiar.objects.filter(nombre=nombrecito)
        # personas=Familiar.objects.filter(nombre__icontains=nombrecito) #Para buscar algo que contenga "nombrecito", es una busqueda NO exacta.

        if len(personas)!=0:
            return render(request, "MVT_DALINGER_App/resultado_busqueda.html", {"personas":personas, "nombre_buscado":nombrecito})
        else:
            return render(request, "MVT_DALINGER_App/resultado_busqueda.html", {"mensaje":"No existe esa persona en base de datos", "nombre_buscado":nombrecito})
    else:
        return render(request, "MVT_DALINGER_App/busqueda_edad.html", {"mensaje":"No pusiste datos. Vuelva a cargar."})

