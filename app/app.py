from flask import Flask, request
import os
# Importamos esto para simular la validacion 
import socket
import logging
import sys

# --- CONFIGURACIÓN DE LOGS ---
# Configuramos el logger para que escriba en sys.stdout donde Docker los visualiza
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("backend-service")

app = Flask(__name__)

# Loguea cada petición que entra para tener trazabilidad
@app.before_request
def log_request_info():
    logger.info(f"Petición: {request.method} {request.url} - IP: {request.remote_addr}")

@app.route("/")
def hello():
    message = f"Hello from {os.getenv('ENV', 'dev')}!"
    logger.info("Respondiendo a la ruta raíz")
    return message

# --- SECCIÓN DE HEALTH CHECK ---
@app.route("/health")
def health_check():
    # Logueamos cuando el Health Check es consultado
    logger.info("Health check consultado - Estado: OK")
	# retornamos 200 OK para que Docker sepa que el proceso vive 
    return {"status": "healthy", "container": socket.gethostname()}, 200

if __name__ == "__main__":
    logger.info("Iniciando servidor Flask en el puerto 5000...")
    app.run(host="0.0.0.0", port=5000)
