from dataclasses import fields
from django.forms import ModelForm
from gimnasio.models import Asistencia, Membresia, Notificacion
from django import forms

class AsistenciaForm(ModelForm):
    class Meta:
        model = Asistencia
        fields = '__all__'

class MembresiaForm(ModelForm):
    class Meta:
        model = Membresia
        fields = '__all__'

class NotificacionForm(ModelForm):
    class Meta:
        model = Notificacion
        fields = '__all__'

