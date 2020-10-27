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