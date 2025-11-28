from django.db import models
from datetime import datetime
from decimal import Decimal
# Create your models here.

































































































































































































































































































































class Rutina(models.Model):
    tipo = models.CharField(
        max_length=50,
        choices=[
            ('FUERZA', 'Fuerza'),
            ('CARDIO', 'Cardio'),
            ('MIXTA', 'Mixta'),
            ('FUNCIONAL', 'Funcional'),
        ],
        db_index=True
    )

    disponibilidad = models.IntegerField(
        default=1,
        db_index=True
    )

    distribucion = models.CharField(
        max_length=30,
        choices=[
            ('SUPERIOR', 'Superior'),
            ('INFERIOR', 'Inferior'),
            ('COMPLETA', 'Cuerpo completo'),
            ('HIIT', 'HIIT'),
        ]
    )

    id_imc = models.ForeignKey(
        'Imc',
        on_delete=models.SET_NULL,
        null=True,
        db_index=True
    )

    intensidad = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        default=Decimal('0.0')
    )

    class Meta:
        db_table = 'rutinas'
        indexes = [
            models.Index(fields=['tipo'], name='idx_tipo_rt'),
            models.Index(fields=['disponibilidad'], name='idx_disp_rt'),
            models.Index(fields=['id_imc'], name='idx_imc_rt'),
            models.Index(fields=['tipo', 'disponibilidad'], name='idx_tipo_disp'),
        ]

    def __str__(self):
        return f"Rutina {self.id}"
