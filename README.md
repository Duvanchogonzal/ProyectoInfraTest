# Prueba Técnica - Infraestructura / DevOps

## Objetivo
Levantar el entorno y hacer que la aplicación sea accesible en:

http://localhost:8080

## Problema
Actualmente el sistema NO funciona correctamente.

## Tareas

1. Levantar el entorno
2. Identificar errores
3. Corregirlos
4. Documentar:
   - Qué fallaba
   - Cómo lo solucionaste
## Bonus

- Mejorar Dockerfile * 5 modificaciones
- Agregar healthcheck * se agrego un healthchek en app.apy y docker-compose.yml
- Logs claros * se ordenan los logs y se toman capturas de healthcheck y peticiones desde app.py para ser mas facil la visualizacion  
- Preparar despliegue * se prepara el archivo docker compose para el despliqgue se condifura polita de resiliencia , limitacion de consumo
 de recursos e inteligencia despliqgue, si no funciona el backend nginx no inicia. 
- levantar servicio con traefik y modo swarm de docker
- integración continua

##Solucion

- En el archivo docker compose.yml

	- En el encabezado la etiqueta version es obsoleta esto ya no es necesario poner la version.
		-version: '3.8'
	- En el modulo de service en el apartado donde definimos el nombre esta como "web:" pero en el
 archivo nginx/default.config el servicio esta declarado como backend al igual que la declaracion depends_on: que esta backend. Por eso lo remplazamos por backend:
		
	services:
 	 backend:  #  Cambiado de 'web' a 'backend'
   	 build: ./app
    	container_name: app
   	 environment:
      - ENVIRONMENT=production
   		 expose:
      - "5000"

	
	depends_on:
      - backend  # Ahora sí coincide con el nombre de arriba

- Archivo nginx/default.config
	
	- En el apartado "location" esta mal asignado el puerto.

	location / {
        proxy_pass http://backend:8000;
    	}


	Lo correcto es que este asignado el puerto 5000 que es el que se le asigno al servicio en el docker compose.YML

	location / {
        proxy_pass http://backend:5000;
    	}


	#Con esto ya tenemos la aplicacion funcionando correctamente
