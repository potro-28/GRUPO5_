
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
from django.utils import timezone

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
        widgets = {
            'fecha_registro': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'fk_usuario': forms.Select(attrs={
                'class': 'form-control',
            }),
        }
    def clean_fecha_registro(self):
        fecha_registro = self.cleaned_data['fecha_registro']
        if fecha_registro < timezone.now().date():
            raise forms.ValidationError("La fecha de registro no puede ser en el pasado.")
        return fecha_registro
        
class TurnodeentrenadorForm(ModelForm):
    class Meta:
        model = Turnosentrenadores
        fields = '__all__'
        widgets = {
            'fecha_turno_inicio': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'fecha_turno_final': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'jornada': forms.Select(attrs={
                'class': 'form-control',
            }),
        }
        
    def clean_fecha_turno_inicio(self):
        fecha_turno_inicio = self.cleaned_data['fecha_turno_inicio']
        if fecha_turno_inicio < timezone.now().date():
            raise forms.ValidationError("La fecha de inicio del turno no puede ser en el pasado.")
        return fecha_turno_inicio
    
    def clean_fecha_turno_final(self):
        fecha_turno_inicio = self.cleaned_data.get('fecha_turno_inicio')
        fecha_turno_final = self.cleaned_data['fecha_turno_final']
        if fecha_turno_final < timezone.now().date():
            raise forms.ValidationError("La fecha de finalización del turno no puede ser en el pasado.")
        if fecha_turno_inicio and fecha_turno_final < fecha_turno_inicio:
            raise forms.ValidationError("La fecha de finalización del turno no puede ser anterior a la fecha de inicio.")
        return fecha_turno_final
        

class CertificacioninternaForm(ModelForm):
    class Meta:
        model = Certificacion_interna
        fields = '__all__'
        widgets = {
            'fecha_certificacion': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'descripcion_certificacion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la descripcion de la certificacion interna'
            }),
            'fk_Asistencia': forms.Select(attrs={
                'class': 'form-control',
            }),
        }
    def clean_descripcion_certificacion(self):
        descripcion_certificacion = self.cleaned_data['descripcion_certificacion']
        if len(descripcion_certificacion) < 10:
            raise forms.ValidationError("La descripcion de la certificacion interna debe tener al menos 10 caracteres.")
        if descripcion_certificacion.isdigit():
            raise forms.ValidationError("La descripcion de la certificacion interna no puede ser solo números.")
        return descripcion_certificacion
    
    def clean_fecha_certificacion(self):
        fecha_certificacion = self.cleaned_data['fecha_certificacion']
        hoy = timezone.now().date()
        if fecha_certificacion < hoy:
            raise forms.ValidationError(
            "La fecha de certificación no puede ser una fecha pasada."
        )
        if fecha_certificacion > hoy:
            raise forms.ValidationError(
            "La fecha de certificación no puede ser una fecha futura."
        )
        return fecha_certificacion    