from django.shortcuts import render
# importamos vistas:
from django.views.generic import (
    ListView
    )
# Importamos models:
from .models import Empleado

# Create your views here.

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    model = Empleado

class ListByArea(ListView):
    """Lista de empleados de un área de la empresa"""
    template_name = 'persona/list_by_area.html'
    # En vez de pasarle el model completo, hacemos una query
    # al mismo tiempo generamos un filtro en el template
    queryset = Empleado.objects.filter(
        departamento__short_name = 'Otro'
    )