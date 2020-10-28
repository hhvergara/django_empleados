from django.db import models
# Importamos el modelo "Departamento" de la app departamento
# Para poder importar la FK
from applications.departamento.models import Departamento
# Create your models here.


class Empleado(models.Model):
    """Model definition for Empleado."""
    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO')
    )

    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellido', max_length=60)
    # Agregamos una tupla de opciones de trabajo:
    # Contador
    # Administrador
    # Economista
    # Otro
    job = models.CharField('Trabajo', max_length=60, choices=JOB_CHOICES)
    # Creamos la foreign key (FK):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # image = models.ImageField('image', upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        """Unicode representation of Empleado."""
        return f'{self.id} - {self.first_name} - {self.last_name}'
