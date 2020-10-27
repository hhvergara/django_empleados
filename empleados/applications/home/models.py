from django.db import models

# Create your models here.
# Este es el documento que trabaja con las bases de datos en django
#  Django utiliza ORM para el manejo de la base de datos, no SQL... 


# creamos la clase prueba, no explicó bien qué hace cada cosa, solo lo creo.
class Prueba(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.titulo + ' ' + self.subtitulo