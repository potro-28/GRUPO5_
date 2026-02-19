
from dataclasses import fields
from gimnasio.models import Elemento, Usuario, Mantenimiento
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
from django.forms import ModelForm
from gimnasio.models import Masa_corporal
from django.forms import ModelForm
from gimnasio.models import Sancion
from django.forms import ModelForm
from gimnasio.models import Registrovisitantestemporales
from gimnasio.models import Turnosentrenadores
from gimnasio.models import Certificacion_interna

class ElementoForm(forms.ModelForm):
    class Meta:
        model = Elemento
        fields = '__all__'


class usuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = '__all__'
widgets = {
            'fecha_programada':forms.DateInput(attrs={'type': 'date'}),
            'fecha_realizada': forms.DateInput(attrs={'type': 'date'}),
        }


class AsistenciaForm(ModelForm):
    

    class Meta:
        model = Asistencia
        fields = '__all__'
        widgets = {
            'fecha_asistencia': forms.DateInput(attrs={ 
                'class': 'form-control',
                'type': 'date'
            }),
        }
    def clean(self):
        cleaned_data = super().clean()
        hora_entrada = cleaned_data.get('hora_ingreso')
        hora_salida = cleaned_data.get('hora_salida')

        if hora_salida == hora_entrada:
            raise forms.ValidationError('La hora de salida no puede ser igual a la hora de entrada')
        if hora_salida < hora_entrada:
            raise forms.ValidationError('La hora de salida no puede ser anterior a la hora de entrada')

        return cleaned_data
    
class MembresiaForm(ModelForm):
    class Meta:
        model = Membresia
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={ 
                'class': 'form-control',
                'type': 'date'
            }),
            'fecha_fin': forms.DateInput(attrs={ 
                'class': 'form-control',
                'type': 'date'
            }),
        }
        
    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')
        fk_usuario = cleaned_data.get('fk_usuario')
        if fecha_fin == fecha_inicio:
            raise forms.ValidationError('La fecha de finalización no puede ser igual a la fecha de inicio')
        if fecha_fin < fecha_inicio:
            raise forms.ValidationError('La fecha de finalización no puede ser anterior a la fecha de inicio')
        if fk_usuario.membresia_set.filter(fecha_inicio__month=fecha_inicio.month, fecha_inicio__year=fecha_inicio.year).exists():
            raise forms.ValidationError('El usuario ya tuvo una membresia este mismo mes')
        return cleaned_data
    
    

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


class Masa_muscularForm(ModelForm):
    class Meta:
        model = Masa_corporal
        fields = '__all__'

class SancionesForm(ModelForm):
    class Meta:
        model = Sancion
        fields = '__all__'


class RegistrovisitantetemporalForm(ModelForm):
    class Meta:
        model = Registrovisitantestemporales
        fields = '__all__'
        
class TurnodeentrenadorForm(ModelForm):
    class Meta:
        model = Turnosentrenadores
        fields = '__all__'
        
class CertificacioninternaForm(ModelForm):
    class Meta:
        model = Certificacion_interna
        fields = '__all__'
