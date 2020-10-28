from django.contrib import admin
# importamos el modelo empleados
from .models import Empleado
# Register your models here.
admin.site.register(Empleado)