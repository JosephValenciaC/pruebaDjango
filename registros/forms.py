
from django import forms
from .models import Alumnos, ComentarioContacto

class ComentarioContactoForm(forms.ModelForm):
    class Meta:
        model = ComentarioContacto
        fields = ('usuario', 'mensaje')

class AlumnosForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ('matricula','nombre', 'carrera', 'turno')