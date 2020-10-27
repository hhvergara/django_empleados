from django.shortcuts import render
# Importamos vistas genericas:
from django.views.generic import (TemplateView, 
    ListView, 
    CreateView
    )
# Importamos la base de datos "Pueba" desde el model
from .models import Prueba


# Create your views here.
# Probamos la vista generica:
class PruebaView(TemplateView):
    template_name = 'home/prueba.html'

class PruebaListView(ListView):
    template_name = 'home/lista.html'
    context_object_name = 'listanumeros' # así podemos declarar una variable en el front
    # Podemos usar el Queryset para traer elementos de una lista:
    queryset  = ['0','10','20','30']

class ListarPrueba(ListView):
    template_name = "home/lista-prueba.html"
    # Aquí le decimos que model vamos a usar, debe ser del model de la carpeta de la aplicación
    model = Prueba
    # con esto obtenemos los registros de la query
    context_object_name = 'lista'


class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    # Aquí le decimos por medio de una lista qué parámetros son los que queremos ingresar:
    fields = ['titulo', 'subtitulo', 'cantidad']
