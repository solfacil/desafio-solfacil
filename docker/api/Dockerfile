FROM python:3.9

WORKDIR /code

RUN apt update && apt upgrade -y
RUN pip install --upgrade pip

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 9092

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload", "--port", "9092"]
