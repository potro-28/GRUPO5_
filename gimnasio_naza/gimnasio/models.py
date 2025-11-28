from django.db import models
from datetime import datetime
from decimal import Decimal
# Create your models here.

































































































































































































































































































































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
    
class Registro_Visitantes(models.Model):
    fecha_registro = models.DateField(default=datetime.now)
    fk_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def _str_(self):
        return self.id

    class Meta:
        verbose_name = 'Registro_Visitante'
        verbose_name_plural = 'Registro_Visitantes'
        db_table = 'registro_Visitantes'
        
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