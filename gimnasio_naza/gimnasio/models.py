from django.db import models

# Create your models here.









































































































































from django.db import models
from datetime import datetime
#--------------------------------Modulo de Gestión de Encuestas----------------------------
class Encuesta(models.Model):
    ESTADO_CHOICES = [
        ('A', 'Activa'),
        ('I', 'Inactiva'),
    ]

    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=1,choices=ESTADO_CHOICES,default='A')
    fk_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='Encuestas')
    
    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Encuesta'
        verbose_name_plural = 'Encuestas'
        db_table = 'Encuesta'
        
#--------------------------------Modulo de Gestión de reportes y estadistica------------------------
class Reportes_estadistica(models.Model):
    TIPO_REPORTE_CHOICES = [
        ('membresia', 'Membresía'),
        ('asistencia', 'Asistencia'),
        ('elemento', 'Elemento'),
    ]
    FORMATO_CHOICES = [
        ('pdf', 'pdf'),
        ('excel', 'excel'),
    ]
    tipo_reporte = models.CharField(max_length=20,choices=TIPO_REPORTE_CHOICES,default='membresia')
    fecha_generacion = models.DateField(default=datetime.now)
    formato = models.CharField(max_length=10,choices=FORMATO_CHOICES,default='pdf')
    fk_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='Reportes')

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Reporte'
        verbose_name_plural = 'Reportes'
        db_table = 'Reporte'

#--------------------------------Modulo Gestión de reportes y PQRS------------------------
class Soporte_PQRS(models.Model):
    TIPO_PQRS_CHOICES = [
        ('peticion', 'Petición'),
        ('queja', 'Queja'),
        ('reclamo', 'Reclamo'),
        ('sugerencia', 'Sugerencia'),
    ]
    tipo = models.CharField(max_length=20,choices=TIPO_PQRS_CHOICES,default='peticion')
    descripcion = models.TextField()
    fecha_ingreso = models.DateField(default=datetime.now)
    ESTADO_CHOICES = [
    ('pendiente', 'pendiente'),
    ('en_proceso', 'en_proceso'),
    ('solucionada', 'solucionada'),
    ]

    estado = models.CharField(
    max_length=20,
    choices=ESTADO_CHOICES,
    default='pendiente'
    )
    fk_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='PQRS')

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'PQRS'
        verbose_name_plural = 'PQRS'
        db_table = 'PQRS'





