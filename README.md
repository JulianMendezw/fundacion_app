# Acerca de fundacion logging app
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

##Interfaz principal
![explorer_XELB8GJgA7](https://github.com/JulianMendezw/fundacion_app/assets/7661539/9b951768-606a-4206-8dbf-d14f38ed30da)


##Mensaje de error

![chrome_5EM3tCvwzh](https://github.com/JulianMendezw/fundacion_app/assets/7661539/445d55a5-4112-4d25-964e-566b1d94a29c)


##Interfaz de acceso
![chrome_vhyrkUPAZ8](https://github.com/JulianMendezw/fundacion_app/assets/7661539/bdfa9ffe-444a-41cb-b788-590a1b9600b3)
