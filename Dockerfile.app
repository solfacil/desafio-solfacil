FROM python:3.11-buster

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install "poetry==1.5.1"

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1

COPY pyproject.toml poetry.lock* entrypoint.sh alembic.ini /app/

RUN chmod +x /app/entrypoint.sh

RUN poetry install --no-root --only main

RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

COPY app /app

EXPOSE 8000
