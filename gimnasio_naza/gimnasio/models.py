from django.db import models
from datetime import datetime

# Create your models here.

#---------MODELO ASISTENCIA -----------------------------------------------------
class Asistencia(models.Model):
    fecha_asistencia = models.DateField(default=datetime.now, verbose_name='Fecha de Asistencia')
    hora_ingreso = models.DateTimeField(default=datetime.now, verbose_name='Hora de Ingreso')
    hora_salida = models.DateTimeField(null=True, blank=True, verbose_name='Hora de Salida')
    fk_membresia = models.ForeignKey('Membresia', on_delete=models.CASCADE, verbose_name='Membresía')

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'
        db_table = 'asistencia'

#-----------------------------MODELO MEMBRESIA---------------------------------------------------
class Membresia(models.Model):
    fecha_inicio = models.DateField(default=datetime.now, verbose_name='Fecha de Inicio')
    fecha_fin = models.DateField(null=True, blank=True, verbose_name='Fecha de Finalización')
    fk_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, verbose_name='Usuario')

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Membresía'
        verbose_name_plural = 'Membresías'
        db_table = 'membresia'
        
#---------------------------------MODELO NOTIFCACIONES-----------------------------------------
TIPO_NOTIFICACION = [
    ('MEMBRESIA', 'Membresía'),
    ('MANTENIMIENTO', 'Mantenimiento'),
    ('ASISTENCIA', 'Asistencia'),
]

CANAL_NOTIFICACION = [
    ('SMS', 'SMS'),
    ('CORREO', 'Correo'),
]

class Notificacion(models.Model):
    tipo_notificacion = models.CharField(max_length=120, choices=TIPO_NOTIFICACION, verbose_name='Tipo de Notificación')
    canal_notificacion = models.CharField(max_length=120, choices=CANAL_NOTIFICACION, verbose_name='Canal de Notificación')
    fk_membresia = models.ForeignKey('Membresia', on_delete=models.CASCADE, verbose_name='Membresía')
    fk_asistencia = models.ForeignKey('Asistencia', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Asistencia')
    fk_mantenimiento = models.ForeignKey('Mantenimiento', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Mantenimiento')

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Notificación'
        verbose_name_plural = 'Notificaciones'
        db_table = 'notificaciones'