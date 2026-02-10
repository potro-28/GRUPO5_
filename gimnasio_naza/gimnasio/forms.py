from dataclasses import fields
from django.forms import ModelForm
from gimnasio.models import Asistencia
from django import forms

class AsistenciaForm(ModelForm):
    class Meta:
        model = Asistencia
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ingrese el nombre de la asistencia'}),
            'descripcion': forms.Textarea(attrs={
                    'placeholder': 'Ingrese la desc de la asistencia',
                    'rows' : 12,
                    'cols': 12})
        }