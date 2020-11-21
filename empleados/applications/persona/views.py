from django.shortcuts import render
# importamos vistas:
from django.views.generic import (
    DeleteView,
    ListView,
    CreateView
)
# Importamos models:
from .models import Empleado


class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4  # Con esto paginamos hasta 4 ítems
    model = Empleado


class ListByArea(ListView):
    """Lista de empleados de un área de la empresa"""
    template_name = 'persona/list_by_area.html'
    # En vez de pasarle el model completo, hacemos una query
    # al mismo tiempo generamos un filtro en el template

    def get_queryset(self):
        """Buscador por endpoint (no usar)"""
        # esta función debe retornar una lista

        # Tomamos el endpoint de la url como variable para asignar
        # el criterio de filtrado:
        area = self.kwargs['shortname']

        lista = Empleado.objects.filter(
            departamento__short_name=area
        )
        return lista


class ListEmpledosByKword(ListView):
    """Buscador por formulario"""
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('************************')
        palabra_clave = self.request.GET.get('kword', '')
        print('************', palabra_clave)
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        print('contenido de la lista: ', lista)
        if str(lista) == '<QuerySet []>':
            return [f'No se han encontrado resultados para la busqueda: {palabra_clave}']
        else:
            return lista


class ListaHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        # Le pasamos el id de la tabla del empleado:
        empleado = Empleado.objects.get(id=1)
        print(empleado.habilidades.all())
        return empleado.habilidades.all()


class EmpleadoDetailView(DeleteView):
    model = Empleado
    template_name = 'persona/detail_empleado.html'

    def get_context_data(self, **kwargs):
        """Sobrescribimos esta función, esta es otra manera de retornar otra 
        variable al template"""
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['Titulo'] = 'Empleado del mes'
        return context


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    fields = ('__all__')
    success_url = '.'

    # fields = ['first_name', 'last_name', 'job']

