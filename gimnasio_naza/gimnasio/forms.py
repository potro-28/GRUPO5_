from dataclasses import fields
from django.forms import ModelForm
from gimnasio.models import Asistencia
from django import forms

class AsistenciaForm(ModelForm):
    class Meta:
        model = Asistencia
        fields = '__all__'
