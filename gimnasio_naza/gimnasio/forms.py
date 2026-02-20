import re 
from dataclasses import fields
from gimnasio.models import Elemento, Usuario, Mantenimiento
from django.forms import ModelForm
from gimnasio.models import Asistencia, Membresia, Notificacion
from gimnasio.models import Encuesta, Soporte_PQRS, Reportes_estadisticas, Categoria, Nutricion, Rutina
from django import forms
from django.utils import timezone


class ElementoForm(forms.ModelForm):
    class Meta:
        model = Elemento
        fields = '__all__'
        widgets = {
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date'}),
        }


    def clean(self):
        cleaned_data = super().clean()
        serial = cleaned_data.get('serial')
        nombre_elemento = cleaned_data.get('nombre_elemento')
        fecha_ingreso = cleaned_data.get('fecha_ingreso')

        # Validar que la fecha no sea futura
        if fecha_ingreso and fecha_ingreso > timezone.now().date():
            raise forms.ValidationError('La fecha de ingreso no puede ser futura.')

        # Validar unicidad
        qs = Elemento.objects.all()
        if self.instance and self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if serial and nombre_elemento and qs.filter(serial=serial,nombre_elemento=nombre_elemento).exists():
            raise forms.ValidationError('Ya existe un elemento con ese serial y nombre.')
        return cleaned_data
    def clean_serial(self):
        serial = self.cleaned_data.get('serial')
        if serial and not re.match(r'^[A-Z0-9]{5,10}$', serial):
            raise forms.ValidationError('El serial debe contener entre 5 y 10 caracteres alfanuméricos en mayúsculas.')
        return serial
    def clean_nombre_elemento(self):
        nombre_elemento = self.cleaned_data.get('nombre_elemento')
        if nombre_elemento and not re.match(r'^[a-zA-Z\s]+$', nombre_elemento):
            raise forms.ValidationError('El nombre del elemento solo puede contener letras y espacios.')
        return nombre_elemento
    def clean_fecha_ingreso(self):
        fecha_ingreso = self.cleaned_data.get('fecha_ingreso')
        if fecha_ingreso and fecha_ingreso > timezone.now().date():
            raise forms.ValidationError('La fecha de ingreso no puede ser futura.')
        return fecha_ingreso
    

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_registro': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        documento = cleaned_data.get('documento')
        nombre = cleaned_data.get('nombre')
        apellido = cleaned_data.get('apellido')
        fecha_nacimiento= cleaned_data.get('fecha_nacimiento')
        telefono = cleaned_data.get('telefono')
        correo = cleaned_data.get('correo')
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_registro = cleaned_data.get('fecha_registro')

        # Validar rango de fechas
        if fecha_inicio and fecha_registro:
            if fecha_registro == fecha_inicio:
                raise forms.ValidationError('La fecha de registro no puede ser igual a la fecha de inicio.')
            if fecha_registro < fecha_inicio:
                raise forms.ValidationError('La fecha de registro no puede ser anterior a la fecha de inicio.')

        # Validar unicidad
        qs = Usuario.objects.all()
        if self.instance and self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if documento and nombre and apellido and correo and telefono and fecha_nacimiento and qs.filter(documento=documento, nombre=nombre, apellido=apellido, correo=correo, telefono=telefono, fecha_nacimiento=fecha_nacimiento).exists():
            raise forms.ValidationError('los datos de este usuario ya estan registrados.')

        return cleaned_data
    def clean_documento(self):
        documento = self.cleaned_data.get('documento')
        if documento and not re.match(r'^\d{7,10}$', documento):
            raise forms.ValidationError('El documento debe contener entre 7 y 10 dígitos numéricos.')
        return documento
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre and not re.match(r'^[a-zA-Z\s]+$', nombre):
            raise forms.ValidationError('El nombre solo puede contener letras y espacios.')
        return nombre
    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido')
        if apellido and not re.match(r'^[a-zA-Z\s]+$', apellido):
            raise forms.ValidationError('El apellido solo puede contener letras y espacios.')
        return apellido
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono and not re.match(r'^\d{7,10}$', telefono):
            raise forms.ValidationError('El teléfono debe contener entre 7 y 10 dígitos numéricos.')
        return telefono
    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        if correo and not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', correo):
            raise forms.ValidationError('Ingrese un correo electrónico válido.')
        return correo
    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        if fecha_nacimiento and fecha_nacimiento > timezone.now().date():
            raise forms.ValidationError('La fecha de nacimiento no puede ser futura.')
        return fecha_nacimiento
    

class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = '__all__'
        widgets = {
            'fecha_programada': forms.DateInput(attrs={'type': 'date'}),
            'fecha_realizada': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        fecha_programada = cleaned_data.get('fecha_programada')
        elemento = cleaned_data.get('Elemento')

        # Validar unicidad de mantenimiento por elemento y fecha
        if elemento and fecha_programada:
            qs = Mantenimiento.objects.filter(Elemento=elemento)
            if self.instance and self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)

            if qs.filter(fecha_programada=fecha_programada).exists():
                raise forms.ValidationError('Ya existe un mantenimiento programado para esa fecha en este elemento.')

        return cleaned_data
    
class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = '__all__'

class MembresiaForm(forms.ModelForm):
    class Meta:
        model = Membresia
        fields = '__all__'

class NotificacionForm(forms.ModelForm):
    class Meta:
        model = Notificacion
        fields = '__all__'


class EncuestaForm(forms.ModelForm):
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
        
class Soporte_PQRSForm(forms.ModelForm):
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
        
class Reportes_estadisticasForm(forms.ModelForm):
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
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nombre' : forms.TextInput(attrs={
                'placeholder': 'Ingrese el nombre de la categoria'}),
        }
#Nutricion        
class NutricionForm(forms.ModelForm):
    class Meta:
        model = Nutricion
        fields = '__all__'
        widgets = {
            'nombre' : forms.TextInput(attrs={
                'placeholder': 'Ingrese el nombre de la nutricion'}),
        }
        
#Rutina
class RutinaForm(forms.ModelForm):
    class Meta:
        model = Rutina
        fields = '__all__'
        widgets = {
            'nombre' : forms.TextInput(attrs={
                'placeholder': 'Ingrese el nombre de la rutina'}),
        }
