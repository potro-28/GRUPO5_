
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
import re
from datetime import date
from django.contrib import messages


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

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError("El nombre es obligatorio")

        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombre):
            raise forms.ValidationError(
                'El nombre solo puede contener letras'
            )
        existe = Encuesta.objects.filter(nombre=nombre)

        if self.instance.pk:
            existe = existe.exclude(pk=self.instance.pk)
        if existe.exists():
            raise forms.ValidationError(
                'Ya existe una encuesta con ese nombre'
            )
        return nombre
    
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
    
    #validacion descripcion minimo 10 caracteres   
    def clean_descripcion(self):
        descripcion = self.cleaned_data['descripcion']

        if len(descripcion) < 10:
            raise forms.ValidationError("La descripción debe tener mínimo 10 caracteres")
        if len(descripcion) > 200:
            raise forms.ValidationError("La descripcion  no debe tener mas de 200 caracteres")

        return descripcion
    
    #Validacion fecha de ingreso
    def clean_fecha_ingreso(self):
        fecha_ingreso = self.cleaned_data['fecha_ingreso']
        if fecha_ingreso < date.today():
            raise forms.ValidationError('La fecha de ingreso no puede ser anterior a la de hoy')
        return fecha_ingreso
        
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
    
    def clean_fecha_generacion(self):
        fecha_generacion = self.cleaned_data.get('fecha_generacion')
        if fecha_generacion > date.today():
            raise forms.ValidationError("La fecha no puede ser futura.")
        if fecha_generacion < date(2025, 1, 1):
            raise forms.ValidationError("La fecha no puede ser anterior al 1 de enero de 2025.")
        return fecha_generacion
        
#Categoria
class CategoriaForm(ModelForm):

    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nombre_categoria': forms.TextInput(attrs={
                'class': 'form_control',
                'placeholder': 'Ingrese el nombre de la categoria'
            }),
        }

    #  Validar nombre_categoria
    def clean_nombre_categoria(self):
        nombre = self.cleaned_data.get('nombre_categoria')
        if nombre and not nombre.isalpha():
            raise forms.ValidationError("El Nombre no puede contener números")
        return nombre

    # Validar material
    def clean_material(self):
        material = self.cleaned_data.get('material')
        if material and not material.isalpha():
            raise forms.ValidationError("El Material no puede contener números")
        return material

    #  Validar peso_equipo
    def clean_peso_equipo(self):
        peso = self.cleaned_data.get('peso_equipo')
        if peso and not str(peso).isdigit():
            raise forms.ValidationError("El Peso_Equipo solo puede contener números")
        return peso

    # Validar descripcion
    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if descripcion:
            if len(descripcion) < 10:
                raise forms.ValidationError("La descripción debe tener al menos 10 caracteres")
            if len(descripcion) > 250:
                raise forms.ValidationError("La descripción no puede tener más de 250 caracteres")
        return descripcion
    
    
    


    
#Nutricion        
class NutricionForm(ModelForm):
    class Meta:
        model = Nutricion
        fields = '__all__'
        widgets = {
            'nombre' : forms.TextInput(attrs={
                'placeholder': 'Ingrese el nombre de la nutricion'}),
            
        }
        

# ---------------- RUTINA ----------------
class RutinaForm(ModelForm):
    class Meta:
        model = Rutina
        fields = '__all__'
        widgets = {
            'tipo': forms.Select(attrs={
                'class': 'form-control'
            }),
            'disponibilidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 7
            }),
        }

    # Validación real del sistema
    def clean_disponibilidad(self):
        disponibilidad = self.cleaned_data.get('disponibilidad')
        if disponibilidad < 1 or disponibilidad > 7:
            self.add_error('disponibilidad', "La disponibilidad debe ser un número entre 1 y 7.")
        return disponibilidad
 #--------------------------------------------------------------------------   

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
