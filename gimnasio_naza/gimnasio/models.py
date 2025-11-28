from django.db import models
from datetime import datetime
from decimal import Decimal  

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
        
 #---------------------------------MODELO USUARIO-----------------------------------------       
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
        
#---------------------------------------MANTENIMIENTO------------------------
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
    elemento = models.ForeignKey(Elemento, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
    
    class Meta:
        verbose_name = 'Mantenimiento'
        verbose_name_plural = 'Mantenimientos'
        db_table = 'mantenimiento'
        
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
class Reportes_estadisticas(models.Model):
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
        
#--------------------CATEGORIA------------------

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=45)
    material = models.CharField(max_length=45)
    peso_equipo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre_categoria
    class Meta:
        db_table = "Categoria"
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        
#--------------------NUTRICION------------------

class Nutricion(models.Model):

    NIVEL_ACTIVIDAD = [
        ('bajo', 'Bajo'),
        ('medio', 'Medio'),
        ('alto', 'Alto'),
    ]

    TIPO_OBJETIVO = [
        ('perder_peso', 'Perder Peso'),
        ('mantener', 'Mantener'),
        ('ganar_masa', 'Ganar Masa Muscular'),
    ]

    TIPO_DIETA = [
        ('keto', 'Keto'),
        ('balanceada', 'Balanceada'),
        ('hiperproteica', 'Hiperproteica'),
    ]

    nivel_actividad = models.CharField(max_length=20, choices=NIVEL_ACTIVIDAD)
    tipo_objetivo = models.CharField(max_length=20, choices=TIPO_OBJETIVO)
    tipo_dieta = models.CharField(max_length=40, choices=TIPO_DIETA)

    fk_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.id 
    
    class Meta:
        db_table = "Nutricion"
        verbose_name = "Nutricion"
        verbose_name_plural = "Nutriciones"
        
#------------RUTINA----------------

class Rutina(models.Model):
    tipo = models.CharField(max_length=50,
        choices=[
            ('FUERZA', 'Fuerza'),
            ('CARDIO', 'Cardio'),
            ('FUNCIONAL', 'Funcional'),
        ],
    )

    disponibilidad = models.IntegerField()

    distribucion = models.CharField(
        max_length=30,
        choices=[
            ('SUPERIOR', 'Superior'),
            ('INFERIOR', 'Inferior'),
            ('COMPLETA', 'Cuerpo completo'),
        ]
    )

    fk_imc = models.ForeignKey(Masa_corporal,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Rutina'
        verbose_name_plural = 'Rutinas'
        db_table = 'rutina'

    def __str__(self):
        return self.id
      
#------------REGISTRO DE VISITANTES----------------
    
class Registro_Visitantes(models.Model):
    fecha_registro = models.DateField(default=datetime.now)
    fk_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def _str_(self):
        return self.id

    class Meta:
        verbose_name = 'Registro_Visitante'
        verbose_name_plural = 'Registro_Visitantes'
        db_table = 'registro_Visitantes'

#-----------TURNO DE ENTRENADORES----------------

class Turno_Entrenadores(models.Model):
    JORNADA_CHOICES = [
    ('mañana', 'mañana'),
    ('tarde', 'tarde'),
    ]

    fecha_turno_inicio = models.DateField(default=datetime.now)
    fecha_turno_final = models.DateField(default=datetime.now)
    jornada = models.CharField(max_length=10,choices=JORNADA_CHOICES)

    def __str__(self):
        return self.id

class Meta:
    verbose_name = "Turno Entrenador"
    verbose_name_plural = "Turnos Entrenadores"
    db_table = "turno_entrenadores"
