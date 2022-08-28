from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Familiar)

#Los siguientes no los uso porque son ejemplos de la clase:
    # admin.site.register(Curso)
    # admin.site.register(Estudiantes)
    # admin.site.register(Profesor)
    # admin.site.register(Entregables)