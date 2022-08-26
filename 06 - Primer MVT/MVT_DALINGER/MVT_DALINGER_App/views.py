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
    # texto_1 = f"Familiar creado --> nombre: {familiar_1.nombre} edad: {familiar_1.edad} fecha_alta: {familiar_1.fecha_alta}"

    familiar_2 = Familiar(nombre="jony", edad=28, fecha_alta="1993-11-6")
    familiar_2.save()
    # texto_2 = f"Familiar creado --> nombre: {familiar_2.nombre} edad: {familiar_2.edad} fecha_alta: {familiar_2.fecha_alta}"

    familiar_3 = Familiar(nombre="maxi", edad=28, fecha_alta="1993-11-6")
    familiar_3.save()
    # texto_3 = f"Familiar creado --> nombre: {familiar_3.nombre} edad: {familiar_3.edad} fecha_alta: {familiar_3.fecha_alta}"

    # texto_concatenado = texto_1 + "<br/>" + texto_2 + "<br/>" + texto_3
    # return HttpResponse(texto_concatenado)

    # LO SIGUIENTE FUE LO COMENTADO PARA MODIFICAR SEGUN EL TUTOR, PORQUE SOLO REFLEJABA LOS NOMBRES EN EL template_1.html: 
    # lista_familiar_nombre = [familiar_1.nombre, familiar_2.nombre, familiar_3.nombre] 
    # lista_familiar_edad = [familiar_1.edad, familiar_2.edad, familiar_3.edad]    
    # lista_familiar_fecha_alta = [familiar_1.fecha_alta, familiar_2.fecha_alta, familiar_3.fecha_alta]
    # diccionario = {"lista_nombres":lista_familiar_nombre, 
    #                 "lista_edades": lista_familiar_edad,
    #                 "lista_fecha_altas": lista_familiar_fecha_alta}
    # plantilla = loader.get_template("template_1.html")
    # documento = plantilla.render(diccionario)
    # return HttpResponse(documento)

    familiares = [familiar_1, familiar_2, familiar_3] 

    diccionario = {"familiares":familiares}

    plantilla = loader.get_template("template_1.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)