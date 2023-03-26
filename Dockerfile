# FROM python:3.9 as build
FROM python:3.9.16-slim-bullseye as build

WORKDIR /code

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src/app app

# COPY ./src/app/static app/static
# COPY ./src/app/templates app/templates


EXPOSE 5000

CMD ["python", "app/main.py"]