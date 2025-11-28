from django.db import models
from datetime import datetime

# Create your models here.
#---------MODELO ASISTENCIA -----------------------------------------------------
class Asistencia(models.Model):
    fecha_asistencia = models.DateField(default=datetime.now, verbose_name='Fecha de Asistencia')
    hora_ingreso = models.DateTimeField(default=datetime.now, verbose_name='Hora de Ingreso')
    hora_salida = models.DateTimeField(null=True, blank=True, verbose_name='Hora de Salida')
    fk_membresia = models.ForeignKey(Membresia, on_delete=models.CASCADE)


    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'
        db_table = 'asistencia'

#-----------------------------MODELO MEMBRESIA---------------------------------------------------
class Membresia(models.Model):
    fecha_inicio = models.DateField(default=datetime.now, verbose_name='Fecha de Inicio')
    fecha_fin = models.DateField(null=True, blank=True, verbose_name='Fecha de Finalizacion')
    fk_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Membresia'
        verbose_name_plural = 'Membresias'
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
    tipo_notificacion = models.CharField(max_length=120, choices=TIPO_NOTIFICACION, verbose_name='Tipo de Notificacion')
    canal_notificacion = models.CharField(max_length=120, choices=CANAL_NOTIFICACION, verbose_name='Canal de Notificacion')
    fk_membresia = models.ForeignKey(Membresia, on_delete=models.CASCADE)
    fk_asistencia = models.ForeignKey(Asistencia, on_delete=models.CASCADE)
    fk_mantenimiento = models.ForeignKey(Mantenimiento, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id
      
    class Meta:
        verbose_name = 'Notificacion'
        verbose_name_plural = 'Notificaciones'
        db_table = 'notificaciones'
        
#--------------------------------Modulo de Gestión de Encuestas----------------------------
class Encuesta(models.Model):
    ESTADO_CHOICES = [
        ('A', 'Activa'),
        ('I', 'Inactiva'),
    ]

    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=1,choices=ESTADO_CHOICES,default='A')
    fk_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
       
      
    def __str__(self):
        return self.id
      
    class Meta:
        verbose_name = 'Encuesta'
        verbose_name_plural = 'Encuestas'
        db_table = 'encuesta'
   
 #--------------------------------Modulo Gestión de reportes y PQRS------------------------
     TIPO_REPORTE_CHOICES = [
        ('membresia', 'Membresia'),
        ('asistencia', 'Asistencia'),
        ('elemento', 'Elemento'),
    ]
    FORMATO_CHOICES = [
        ('pdf', 'pdf'),
        ('excel', 'excel'),
    ]
    tipo_reporte = models.CharField(max_length=20,choices=TIPO_REPORTE_CHOICES,default='membresia')
    fecha_generacion = models.DateField(default=datetime.now)
    formato = models.CharField(max_length=10,choices=FORMATO_CHOICES)
    fk_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Reporte'
        verbose_name_plural = 'Reportes'
        db_table = 'Reporte'

#--------------------------------Modulo Gestión de reportes y PQRS------------------------
class Soporte_PQRS(models.Model):
    TIPO_PQRS_CHOICES = [
        ('peticion', 'Peticion'),
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

    estado = models.CharField(max_length=20,choices=ESTADO_CHOICES,default='pendiente')
    fk_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
      return self.id
        
    class Meta:   
        verbose_name = 'PQRS'
        verbose_name_plural = 'PQRS'
        db_table = 'PQRS'
  
 
        
        


