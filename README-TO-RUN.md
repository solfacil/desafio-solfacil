## Amaterasu API - Partners Loader

### **Technologies/Frameworks/Libs used:**

- python "^3.10"
- FastAPI - web framework
- uvicorn - server client
- pydantic - data validation
- loglifos - logs
- python-decouple - files .env
- httpx - client http async
- sqlalchemy["asyncio"] - ORM
- asyncpg - driver prostgres
- pandas - .csv and dataframes handler
- strenum - enumerator handler

### Step one
#### install poetry, if you already have skip.


Linux:
```bash
    curl -sSL https://install.python-poetry.org | python3 -
```

Windows:
```bash
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

### Step two
#### create a virtual environment

- To create the virtual environment and activate, run:
```bash
poetry shell
```


### Step three
#### Installation of dependencies
- Install the packages in the virtual environment from the following command:
    
```bash
poetry install
```  

### Step four
#### Create environment variables

- Create a `.env` file in the project root, following this template:

~~~
POSTGRES_URL="postgresql+asyncpg://postgres:12345@localhost:5432/amaterasu_db" 
# start a container postgres server using docker-compose in next step or use your online string connection from a cloud hosted server.
~~~

### Step five
#### Run docker container

- In project root, open terminal and run:
```bash
docker-compose up -d
```

### Step six
#### Run project

1. To start the uvicorn server you need to be at the project root in the terminal and run the following command
 ~~~
   you can simply run the main.py file to start the server
   
   or setting your command line
   
   uvicorn main:app --host 0.0.0.0 --port 9000
 ~~~

2. You can change the HOST and PORT as you wish.

## **Endpoints:**

### "/api/v1/partners/uploadfile  method=POST"

> _Endpoint to upload a .csv file with partners data_

> _Using /docs: will have an upload button_     

> _Using postman: a request using form-data_

### "/api/v1/partners   method=GET"

> _Endpoint to get all partners in JSON format_



**internal_code available:**

- **SUCCESS=**
  0
- **INVALID_PARAMS=**
  10
- **INVALID_AUTHENTICATION=**
  20
- **INTERNAL_SERVER_ERROR=**
  30
- **UNAUTHORIZED=**
  40
- **DATA_VALIDATION_ERROR=**
  50
- **DATA_NOT_FOUND=**
  51
- **DATA_ALREADY_EXISTS=**
  52
- **DATA_CONVERTER_ERROR=**
  53
- **DATA_DECODER_ERROR=**
  53

## **Documentation/Swagger:**

### "http://{HOST}:{PORT}/docs"

> _Example: "http://localhost:9000/docs"_