from django.contrib import admin
# importamos la tabla "Departamento"
from .models import Departamento

# Register your models here.

admin.site.register(Departamento)