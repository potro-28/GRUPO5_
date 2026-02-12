from dataclasses import field
from django.forms import ModelForm
from gimnasio.models import Categoria
from django import forms
from .models import Nutricion

#Categoria
class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nombre' : forms.TextInput(attrs={
                'placeholder': 'Ingrese el nombre de la categoria'}),
        }
#Nutricion        
class NutricionForm(ModelForm):
    class Meta:
        model = Nutricion
        fields = '__all__'
        widgets = {
            'nombre' : forms.TextInput(attrs={
                'placeholder': 'Ingrese el nombre de la nutricion'}),
        }
        
#Rutina
class RutinaForm(ModelForm):
    class Meta:
        model = Nutricion
        fields = '__all__'
        widgets = {
            'nombre' : forms.TextInput(attrs={
                'placeholder': 'Ingrese el nombre de la rutina'}),
        }