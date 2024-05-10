# Getting Started with fundacion logging app
El proyecto se desarrollo con react para el frontend, python para el backend y como base de datos supabase.

El proyecto contine un archivo dockerfile para la dokerizacion del front

Para el proyecto es requerido Node y python

En el directorio raiz se encuentra el directorio api el cual contine la API desarrollado en Python para la coneccion a la base de datos y el acceso para los usuarios si estan registrados

usuario de prueba:

email: string@email.com
contraseña: 1234

### para levantar el front:
Antes de ejecutar estos comandos debe instalar Node v20.10.0

se debe ubicar en la carpeta raiz del proyecto y ejecutar los siguientes comandos:


para instalar dependencias:
npm i

para levantar el proyecto:
npm start


### Para levantar el back

Se debe ubicar en directorio api y ejecutar los siguientes comandos,
Para ejecutar estos pasos debe instalar python:

pip install -r requirements.txt

para correr el back:

fastapi dev app/main.py

### Ejemplos de la app

Interfaz principal

Mensaje de error

Interfaz de acceso