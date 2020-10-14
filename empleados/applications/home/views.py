from django.shortcuts import render
# Importamos vistas genericas:
from django.views.generic import TemplateView

# Create your views here.
# Probamos la vista generica:
class PruebaView(TemplateView):
    template_name = 'prueba.html'
