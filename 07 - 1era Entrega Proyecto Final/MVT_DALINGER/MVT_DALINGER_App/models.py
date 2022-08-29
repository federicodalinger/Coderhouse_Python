from django.db import models

# Create your models here.

class Familiar (models.Model): # El .Models es para que herede el "models"
    nombre = models.CharField(max_length=50) 
    edad = models.IntegerField() 
    fecha_alta = models.DateField() 

    def __str__(self):
        #ESTO ES COMO VOY A VER MI BASE DE DATOS EN "ADMIN":
        return "Nombre: " + self.nombre + " | Edad: " + str(self.edad) + " | Fecha de alta: " + str(self.fecha_alta) + " |"