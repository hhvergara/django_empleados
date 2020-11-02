from django.db import models

# Create your models here.

# Creamos la tabla de la base de datos "Departamento"
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50, blank=True, unique=True)
    short_name = models.CharField('Nombre Corto', max_length=20)
    anulate = models.BooleanField('anulado', default=False)
    # Se pueden buscar los tipos de campo como "Djangop models fields types" en google
    class Meta:
        verbose_name = 'Mi departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['name'] # -name para hacerlo descendente
        unique_together = ('name', 'short_name')


    def __srt__(self):
        return f'{self.id} - {self.name} - {self.short_name}'
