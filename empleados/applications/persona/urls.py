from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
    # Agregamos el endpoint shortname para que lo levante get_queryset en la view:
    path('lista-by-area/<shortname>/', views.ListByArea.as_view()),
    path('buscar-empleado/', views.ListEmpledosByKword.as_view()),
    path('lista-habilidades-empleado/', views.ListaHabilidadesEmpleado.as_view()),
    path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view()),
    path('add-empleado', views.EmpleadoCreateView.as_view()),

]
