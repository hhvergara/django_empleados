from django.contrib import admin
# importamos el modelo empleados
from .models import Empleado, Habilidades
# Register your models here.
admin.site.register(Habilidades)


# Modelamos el administrador de Django con clases:

class EmpleadosAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'departamento', 'job', 'full_name'
    )
    # Como full_name no está declarado en mi model, lo agregamos aquí,
    # Corresponde a una nueva columna en el administrador de django->persona

    def full_name(self, obj):
        # Agregamos toda la operación que queremos que aparezca en cada celda de la tabla
        return f'{obj.first_name} {obj.last_name}'
        # Agregamos un buscador:
    search_fields = (
        'first_name',
    )
    # Agregamos un filtro por trabajo:
    list_filter = ('departamento', 'job', 'habilidades')
    # Agregamos un filtro horizontal:
    filter_horizontal = ('habilidades',)


admin.site.register(Empleado, EmpleadosAdmin)
