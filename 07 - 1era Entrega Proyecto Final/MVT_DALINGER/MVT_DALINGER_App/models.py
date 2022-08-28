from django.db import models

# Create your models here.

class Familiar (models.Model):
    nombre = models.CharField(max_length=50) 
    edad = models.IntegerField() 
    fecha_alta = models.DateField() 

    def __str__(self):
        return "Nombre: " + self.nombre + " | Edad: " + str(self.edad) + " | Fecha de alta: " + str(self.fecha_alta) + " |"