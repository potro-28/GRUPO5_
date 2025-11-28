


































































































































































































































                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                

from django.db import models

class Usuario(models.Model):
    documento = models.CharField(max_length=45, unique=True)
    nombre_usuario = models.CharField(max_length=45)
    apellido_usuario = models.CharField(max_length=45)
    fecha_nacimiento = models.DateField()
    telefono_usuario = models.CharField(max_length=45)
    correo_usuario = models.CharField(max_length=100, unique=True)
    peso_usuario = models.DecimalField(max_digits=10, decimal_places=2)
    altura_usuario = models.DecimalField(max_digits=10, decimal_places=2)
    ROL_CHOICES = [
        ('cliente', 'Cliente'),
        ('admin', 'Administrador'),
    ]
    rol = models.CharField(max_length=30, choices=ROL_CHOICES)
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('visitante', 'Visitante'),
    ]
    estado = models.CharField(max_length=30, choices=ESTADO_CHOICES)
    fecha_registro = models.DateField()

    def __str__(self):
        return self.id
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuario'
#------ELEMENTO------------------------
class Elemento(models.Model):
    serial = models.CharField(max_length=45, unique=True)
    marca = models.CharField(max_length=45)
    nombre_elemento = models.CharField(max_length=45)
    TIPO_CHOICES = [
        ('maquina', 'Máquina'),
        ('disco', 'Disco'),
        ('mancuerna', 'Mancuerna'),
        ('barra', 'Barras'),
        ('otro', 'Otro'),
    ]
    tipo_elemento = models.CharField(max_length=20, choices=TIPO_CHOICES)
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    fecha_ingreso = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_elemento
    
    class Meta:
        verbose_name = 'Elemento'
        verbose_name_plural = 'Elementos'
        db_table = 'elementos'

class Mantenimiento(models.Model):
    fecha_programada = models.DateField()
    TIPO_CHOICES = [
        ('preventivo', 'Preventivo'),
        ('correctivo', 'Correctivo'),
    ]
    tipo_mantenimiento = models.CharField(max_length=20, choices=TIPO_CHOICES)
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En proceso'),
        ('completado', 'Completado'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    elemento = models.ForeignKey('Elemento', on_delete=models.CASCADE)

    def __str__(self):
        return self.id
    
    class Meta:
        verbose_name = 'Mantenimiento'
        verbose_name_plural = 'Mantenimientos'
        db_table = 'mantenimiento'