# Usar una imagen base de Python
FROM python:3.11-slim

# Instalar dependencias del sistema para psql
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar requirements.txt e instalar dependencias
COPY requirements.txt .
COPY entrypoint.sh /entrypoint.sh
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x /entrypoint.sh

# Copiar el resto del código
COPY . .

RUN python manage.py collectstatic --noinput

# Configurar variables de entorno
ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["/entrypoint.sh"]

# Ejecutar el servidor con gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "App.wsgi:application"]