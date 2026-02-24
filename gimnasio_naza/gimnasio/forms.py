
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
from django.core.exceptions import ValidationError
from django.core.exceptions import ValidationError
from datetime import date , timedelta

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
        widgets = {
            'fecha_control': forms.DateInput(attrs={
                'type': 'date'
            }),
        }

    def clean_peso_cliente(self):
        peso = self.cleaned_data.get('peso_cliente')

        if peso <= 0:
            raise ValidationError("El peso debe ser mayor que 0.")

        if peso < 30 or peso > 300:
            raise ValidationError("El peso debe estar entre 30kg y 300kg.")

        return peso

    def clean_altura_cliente(self):
        altura = self.cleaned_data.get('altura_cliente')

        if altura <= 0:
            raise ValidationError("La altura debe ser mayor que 0.")

        if altura < 0.5 or altura > 2.5:
            raise ValidationError("La altura debe estar entre 0.5m y 2.5m.")

        return altura

    def clean_fecha_control(self):
        fecha = self.cleaned_data.get('fecha_control')
        if fecha > date.today():
            raise ValidationError("La fecha no puede ser futura.")
        if fecha < date(1950, 1, 1):
            raise ValidationError("La fecha no puede ser anterior al 1 de enero de 1950.")
        return fecha

    def clean(self):
        cleaned_data = super().clean()
        fk_nutricion = cleaned_data.get('fk_Nutricion')
        fecha = cleaned_data.get('fecha_control')

        if fk_nutricion and fecha:
            queryset = Masa_corporal.objects.filter(
                fk_Nutricion=fk_nutricion,
                fecha_control=fecha
            )

            if self.instance.pk:
                queryset = queryset.exclude(pk=self.instance.pk)

            if queryset.exists():
                raise ValidationError(
                    "Ya existe un control para esta nutrición en esa fecha."
                )

        return cleaned_data

class SancionesForm(forms.ModelForm):
    class Meta:
        model = Sancion
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }

    # 🔹 Validar que el motivo empiece con letra
    def clean_motivo_sancion(self):
        motivo = self.cleaned_data.get('motivo_sancion')

        if not motivo or len(motivo.strip()) < 5:
            raise ValidationError("El motivo debe tener al menos 5 caracteres.")

        motivo = motivo.strip()

        if not motivo[0].isalpha():
            raise ValidationError("La descripción debe iniciar obligatoriamente con una letra.")

        return motivo

    # 🔹 Validar duración
    def clean_duracion_sancion(self):
        duracion = self.cleaned_data.get('duracion_sancion')

        if duracion <= 0:
            raise ValidationError("La duración debe ser mayor que 0 días.")

        if duracion > 365:
            raise ValidationError("La duración no puede ser mayor a 365 días.")

        return duracion

    # 🔥 AQUÍ HACEMOS LA MAGIA
    def clean(self):
        cleaned_data = super().clean()

        duracion = cleaned_data.get('duracion_sancion')
        usuario = cleaned_data.get('fk_usuario')
        tipo = cleaned_data.get('tipo_sancion')
        estado = cleaned_data.get('estado')

        # 🔹 Forzar fecha_inicio como HOY
        fecha_inicio = date.today()
        cleaned_data['fecha_inicio'] = fecha_inicio

        # 🔹 Calcular fecha_fin automáticamente
        if duracion:
            fecha_fin = fecha_inicio + timedelta(days=duracion)
            cleaned_data['fecha_fin'] = fecha_fin

        # 🔹 Evitar sanciones activas duplicadas
        if usuario and tipo and estado == 'activa':
            queryset = Sancion.objects.filter(
                fk_usuario=usuario,
                tipo_sancion=tipo,
                estado='activa'
            )

            if self.instance.pk:
                queryset = queryset.exclude(pk=self.instance.pk)

            if queryset.exists():
                raise ValidationError(
                    "Este usuario ya tiene una sanción activa de este tipo."
                )

        return cleaned_data

    # 🔹 Validaciones generales
    def clean(self):
        cleaned_data = super().clean()

        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')
        usuario = cleaned_data.get('fk_usuario')
        tipo = cleaned_data.get('tipo_sancion')
        estado = cleaned_data.get('estado')

        # Validar fechas
        if fecha_inicio and fecha_fin:
            if fecha_fin <= fecha_inicio:
                raise ValidationError(
                    "La fecha de fin debe ser mayor que la fecha de inicio."
                )

        # Evitar sanciones activas duplicadas
        if usuario and tipo and estado == 'activa':
            queryset = Sancion.objects.filter(
                fk_usuario=usuario,
                tipo_sancion=tipo,
                estado='activa'
            )

            if self.instance.pk:
                queryset = queryset.exclude(pk=self.instance.pk)

            if queryset.exists():
                raise ValidationError(
                    "Este usuario ya tiene una sanción activa de este tipo."
                )

        return cleaned_data


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