#!/bin/bash
set -e

# Tiempo máximo de espera (en segundos)
MAX_WAIT=30
COUNTER=0

# Esperar a que la base de datos esté lista
if [ -n "$DATABASE_URL" ]; then
    echo "Waiting for PostgreSQL to be available..."
    until psql "$DATABASE_URL" -c '\q' 2>/dev/null; do
        if [ $COUNTER -ge $MAX_WAIT ]; then
            echo "Error: PostgreSQL is not available after $MAX_WAIT seconds"
            exit 1
        fi
        echo "PostgreSQL is not available yet. Waiting..."
        sleep 1
        COUNTER=$((COUNTER + 1))
    done
    echo "PostgreSQL is available."
fi

# Aplicar migraciones
echo "Aplying migrations..."
python manage.py migrate

# Crear superusuario
echo "Creating default superuser..."
python manage.py defaultsuperuser

# Ejecutar el comando pasado
exec "$@"