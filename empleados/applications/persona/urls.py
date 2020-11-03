from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
    path('lista-by-area/', views.ListByArea.as_view())
 
]