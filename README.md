#Comandos para correr el proyecto

Para crear una app de django:

$ ```django-admin startapp nombre_de_la_app ```

Para correr el entorno virtual en bash:

$ ```source ./activate```

Para ejecutar el servidor:

$ ```python manage.py runserver```

Para que el sistema reconozca cambios en el model (db):

$ ```python manage.py makemigrations```

Para que el sistema aplique cambios en el model (db):

$ ```python manage.py migrate```

Para crear un super usuario:

$ ```python manage.py createsuperuser```

En este ejemplo: user: hector, mail hvergara@inove.com.ar, pass: hector01


#Docker compose

Dentro del archivo 'stack.yml' se encuentra el archivo para correr el container de la base de datos Postgres utilizada en el proyecto,
dentro del mismo, se encuentran las instrucciónes para correrlo, pero para poder hacer el build, tenemos que correr el comando:

```docker-compose -f stack.yml up```

De esta manera tendremos montada nuestra base de datos Postgre en nuestro sistema, la cual tiene su administrador 'adminer' en la dirección localhost:8080


#Links útiles:
- Sobre vistas genéricas: https://ccbv.co.uk/
- Editor para campos de admin: pip install django-ckeditor (https://pypi.org/project/django-ckeditor/)
