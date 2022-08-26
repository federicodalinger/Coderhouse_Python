#Importamos lo necesario proyecto:
from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader

from MVT_DALINGER_App.views import nuevo_familiar

def saludo(reauest): #En "reauest" va toda la info que trae del cliente
    return HttpResponse(
        '''Buenas! Para agregar los familiares --> http://127.0.0.1:8000/nuevo_familiar''')