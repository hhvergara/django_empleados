#!/usr/bin/env python
"""Librería de inicialización del proyecto, para inicializar el proyecto"""
import os
import sys
import platform
import subprocess
import json


HOST = ''
Gateway = ''
MacAddress = ''


def define_system():
    system = platform.system()
    print("Estamos en {}".format(system))
    return system


def docker_init():
    """Inicializamos los containers que hacen falta para el proyecto"""
    # using decode() function to convert byte string to string
    if define_system() == 'Linux':
        sudo = 'sudo'
    else:
        sudo = ''

    cmd = f'{sudo} docker inspect postgres_db_1'
    # returns output as byte string
    output = subprocess.check_output(cmd, shell=True)  # capture_output=True
    output = output.decode("utf-8")
    output = json.loads(output)
    HOST = str(output[0]['NetworkSettings']['Networks']['postgres_default']['IPAddress'])
    print(f'IP de database: {HOST}')
    Gateway = output[0]['NetworkSettings']['Networks']['postgres_default']['Gateway']
    MacAddress = output[0]['NetworkSettings']['Networks']['postgres_default']['MacAddress']

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
