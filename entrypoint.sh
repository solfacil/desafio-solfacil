#!/bin/bash

# Wait for postgres to be ready and accepting connections
while ! nc -z postgres12a 5432; do sleep 1; done;

echo "Running migrations"

cd /

alembic -c /app/alembic.ini upgrade head

echo "Starting server"

uvicorn app.main.run_fastapi:app --host 0.0.0.0 --port 8000
