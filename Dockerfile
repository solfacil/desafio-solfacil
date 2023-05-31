FROM python:3.11

WORKDIR /src

COPY ./src/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src .

EXPOSE 3000

CMD ["python", "./frontend/app.py"]