from dataclasses import fields
from django.forms import ModelForm
from gimnasio.models import Asistencia, Membresia, Notificacion
from django import forms
from gimnasio.models import Encuesta
from gimnasio.models import Soporte_PQRS
from gimnasio.models import Reportes_estadisticas
from gimnasio.models import Categoria
from django import forms
from gimnasio.models import Nutricion
from gimnasio.models import Rutina

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




class EncuestaForm(ModelForm):
    class Meta:
        model = Encuesta
        fields = '__all__'
        widgets = {
            'nombre' : forms.TextInput(attrs={ 
                'class':'form-control',
                                           
                'placeholder': 'Ingrese el nombre de la encuesta'}),
            'estado':
                forms.Select(attrs={
                'class':'form-control',  
                'placeholder': 'Ingrese la descripcion de la encuesta',
                'rows':3,
                'cols':3}),
            'fk_usuario':
                forms.Select(attrs={
                    'class':'form-control',
                })      
        }
        
class Soporte_PQRSForm(ModelForm):
    class Meta:
        model = Soporte_PQRS
        fields = '__all__'
        widgets = {
            'tipo' : forms.Select(attrs={ 
                'class':'form-control',
                                           
                'placeholder': 'Ingrese el tipo de soporte pqr'}),
            'descripcion' : forms.TextInput(attrs={ 
                'class':'form-control',
                                           
                'placeholder': 'Ingrese la descripcion del soporte pqr'}),
            'fecha_ingreso': forms.DateInput(attrs={ 
                'class': 'form-control',
                'type': 'date'
            }),
            'estado':
                forms.Select(attrs={
                'class':'form-control',  
                'placeholder': 'Ingrese el estado del soporte pqr',
                'rows':3,
                'cols':3}),
            'fk_usuario':
                forms.Select(attrs={
                    'class':'form-control',
                })      
        }
        
class Reportes_estadisticasForm(ModelForm):
    class Meta:
        model = Reportes_estadisticas
        fields = '__all__'
        widgets = {
            'tipo_reporte': forms.Select(attrs={ 
                'class': 'form-control',
            }),
            'fecha_generacion': forms.DateInput(attrs={ 
                'class': 'form-control',
                'type': 'date'
            }),
            'formato':
                forms.Select(attrs={
                'class':'form-control',  
                'placeholder': 'Ingrese el formato del reporte',
                'rows':3,
                'cols':3}),
            'fk_usuario':
                forms.Select(attrs={
                    'class':'form-control',
                })      
        }
        




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
        model = Rutina
        fields = '__all__'
        widgets = {
            'nombre' : forms.TextInput(attrs={
                'placeholder': 'Ingrese el nombre de la rutina'}),
        }
