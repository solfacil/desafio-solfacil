FROM ubuntu:jammy as python-base
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv" \
    PYTHON_VERSION=3.10

RUN apt-get update -y && \
    apt-get install python${PYTHON_VERSION} python${PYTHON_VERSION}-dev python3-distutils -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"
RUN ln -s /usr/bin/python${PYTHON_VERSION} /usr/bin/python && \
    ln -s /usr/bin/pip3 /usr/bin/pip

FROM python-base as builder

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
        ca-certificates

ENV POETRY_VERSION=1.4.1

RUN curl -sSL https://install.python-poetry.org | python -

WORKDIR $PYSETUP_PATH

COPY ./poetry.lock ./pyproject.toml ./

RUN poetry install --without dev

FROM python-base as development
COPY --from=builder $POETRY_HOME $POETRY_HOME
COPY --from=builder $PYSETUP_PATH $PYSETUP_PATH

COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

WORKDIR $PYSETUP_PATH
RUN poetry install --with dev

WORKDIR /app
COPY . .

EXPOSE 8000

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM development as lint

RUN black --config ./pyproject.toml --check .
RUN flake8

FROM development as test

RUN python manage.py test

FROM python-base as production
LABEL br.com.lbdev.author="Luiz Braga <me@luizbraga.dev>" \
      version="0.1.0" \
      description="Docker image for desafio solfácil."

COPY --from=builder $VENV_PATH $VENV_PATH

COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

WORKDIR /app
COPY . .


EXPOSE 8000

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["gunicorn", "desafio_solfacil.wsgi:application", "--bind", ":8000", "--workers", "3"]

