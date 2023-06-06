FROM python:3
RUN apt-get update
RUN apt-get install -y python3-dev default-libmysqlclient-dev

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD python manage.py runserver 0.0.0.0:8000