from django.contrib import admin
from django.urls import path


def funcion(self):
    '''Funcion creada para que no produzca una excepción'''
    pass

urlpatterns = [
    path('persona/', funcion)
]