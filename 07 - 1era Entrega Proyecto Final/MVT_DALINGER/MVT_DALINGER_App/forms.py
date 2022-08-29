from django import forms

class Familiar_formulario(forms.Form):
    #especificar los campos:
    nombre = forms.CharField(max_length=50) 
    edad = forms.IntegerField() 
    fecha_alta = forms.DateField() 