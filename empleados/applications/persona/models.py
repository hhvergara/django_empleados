from django.db import models
# Importamos el modelo "Departamento" de la app departamento
# Para poder importar la FK
from applications.departamento.models import Departamento
# Importamos el editor de campo de texto:
from ckeditor.fields import RichTextField

# Create your models here.


class Habilidades(models.Model):
    # Esto es parte de una relación N:N de la database, 
    # lo vinculamos con models.ManyToManyField() en Empleado()
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades empleados'

    def __str__(self):
        return f'{self.id} - {self.habilidad}'

class Empleado(models.Model):
    """Model definition for Empleado."""
    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    )

    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellido', max_length=60)
    # Agregamos una tupla de opciones de trabajo:
    # Contador Administrador Economista Otro
    job = models.CharField('Trabajo', max_length=60, choices=JOB_CHOICES)
    # Creamos la foreign key (FK):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # image = models.ImageField('image', upload_to=None, height_field=None, width_field=None, max_length=None)
    
    #hacemos la relación N:N con la tabla Habilidades()
    habilidades = models.ManyToManyField(Habilidades)
    # Agregamos un campo con editor de texto de campo:
    hoja_vida = RichTextField()


    class Meta:
        verbose_name = 'Mi empleado'
        verbose_name_plural = 'Empleados de la empresa'
        # -name para hacerlo descendente
        ordering = ['-first_name', 'last_name']
        unique_together = ('first_name', 'departamento')

    def __str__(self):
        """Unicode representation of Empleado."""
        return f'{self.first_name} - {self.last_name}'
