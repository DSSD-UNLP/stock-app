# stock-app
Sistema de stock para la etapa 1 de la materia DSSD-Unlp
 
## Tecnologías

- Python 3
- Django Framework
- Django Rest Framework

## Guia de instalacion

Para poder correr localmente la aplicación hay ciertas dependencias que deben ser instaladas.
En primer lugar, utilizamos Python 3, se puede chequear ejecutando python --v en la consola.
Si se tiene cualquier version 2.x se debe actualizar.

Utilizamos pip como gestor de paquetes.

- Django : pip install django
- Django Rest Framework : pip install djangorestframework

Dependiendo el motor de base de datos a utilizar, se deberá elegir entre diferentes paquetes, en nuestro caso MySQL requiere:

- MySQL : pip install mysql
- MySQL Client : pip install mysqlclient

Una vez que no queden dependencias por instalar (si es necesario otro paquete la consola lo indicará como feedback, junto con el comando necesario para instalarlo), hay que hacer las migraciones, para esto se ejecuta en orden:

- python3 manage.py makemigrations
- python3 manage.py migrate

## Corriendo la aplicación

Se debe levantar un server ejecutando el comando

'python3 manage.py runserver' (python3 puede reemplazarse por python dependiendo la instalación del mismo).

Ya se puede empezar a hacer requests a la api.
