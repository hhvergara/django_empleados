#!/usr/bin/env python
"""Librería de inicialización del proyecto, para inicializar el proyecto"""
import os
import sys
import platform
import subprocess
import json


def define_system():
    system = platform.system()
    print("Estamos en {}".format(system))
    return system


def docker_init():
    """Inicializamos los containers que hacen falta para el proyecto"""
    if define_system() == 'Linux':
        sudo = 'sudo'
    else:
        sudo = ''

    try:
        os.system(f'{sudo} docker restart postgres_adminer_1')
        os.system(f'{sudo} docker restart postgres_db_1')
        print('hvLog: Inicialización de base de datos exitosa')

    except:
        print('hvLog: fallo de inicialización de base de datos, se intentará descargar imagenes')
        try:
            os.system(f'{sudo} docker pull hhvergara/postgres_adminer_1')
            os.system(f'{sudo} docker pull hhvergara/postgres_db_1')
            os.system(f'{sudo} docker restart postgres_adminer_1')
            os.system(f'{sudo} docker restart postgres_db_1')
            print('hvLog: Inicialización de base de datos exitosa')
        except:
            print('hvLog: fallo en conectarse a la base de datos, verificar dependencias')
