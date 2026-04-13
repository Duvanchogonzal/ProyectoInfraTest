# Usamos una imagen mas simple  "Slim" con esto la imagen que da mucho mas ligera.
FROM python:3.10-slim

# Definimos variables de entorno  para optimizar Python en contenedores con esto python no crea los archivos de cache ya que no es neceario en docker al ser efimeros.


ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Aprovechamos el "Layer Caching" (Instalamos dependencias antes de copiar el código esto con el fin de que docker no vuelva a realizar la instalacion de dependencia)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Creamos un usuario sin privilegios para no correr como root, aqui aplicamos el principio de minimos privilegios

RUN useradd -m myuser
USER myuser

COPY . .

# Documuentamos el puerto esto solo es de manera informativa
EXPOSE 5000


CMD ["python", "app.py"]

