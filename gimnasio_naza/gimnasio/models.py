# core/models.py
from django.db import models





















































































































































































































































































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
        return f"Nutrición de {self.fk_Usuario}"
class Meta:
        db_table = "Nutricion"
        verbose_name = "Nutricion"
        verbose_name_plural = "Nutriciones"