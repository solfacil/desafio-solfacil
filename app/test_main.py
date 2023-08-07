from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .database.connection import Base
from .main import app, get_database

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_database():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_database] = override_get_database
client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.template.name == 'index.html'

def test_read_inexistent_customer():
    response = client.get("/search-customer/1000")
    assert response.status_code == 404
    assert response.json() == {"detail": "Customer not found"}

def test_import_customers():
    file = open("./app/templates/static/emptyfile.csv", "rb")
    response = client.post(
        "/import-customers-from-csv/",
        files={"file": ("filename", file, "image/jpeg")}
    )

    assert response.status_code == 422
    data = response.json()
    assert "detail" in data

    response = client.post(
        "/import-customers-from-csv/",
        files={"upload_file": ("filename", file, "image/jpeg")}
    )

    assert response.status_code == 415
    data = response.json()
    assert "detail" in data
    assert data["detail"] == 'Invalid file received, only .csv files are accepted'

    response = client.post(
        "/import-customers-from-csv/",
        files={"upload_file": ("filename", file, "text/csv")}
    )

    assert response.status_code == 200
    data = response.json()
    assert "detail" in data
    assert "status" in data["detail"] and "messages" in data["detail"]
    assert data["detail"]["status"] == "ERROR"

    response = client.post(
        "/import-customers-from-csv/",
        files={"upload_file": ("filename", file, "text/csv")}
    )

    assert response.status_code == 200
    data = response.json()
    assert "detail" in data
    assert "status" in data["detail"] and "messages" in data["detail"]
    assert data["detail"]["status"] == "SUCCESS"
    file.close()

def test_list_customers():
    response = client.get("/list-customers/")
    assert response.status_code == 200
    assert response.json() == [{'razao_social': 'Sol Eterno', 'email': 'atendimento@soleterno.com', 'nome_fantasia': 'Sol Eterno LTDA', 'telefone': '(21) 98207-9901', 'cpf': None, 'cnpj': '16.470.954/0001-06', 'cliente_id': 1, 'enderecos': [{'cep': '22783-115', 'logradouro': 'Estrada dos Bandeirantes', 'complemento': 'de 7995 a 8901 - lado ímpar', 'bairro': 'Jacarepaguá', 'localidade': 'Rio de Janeiro', 'uf': 'RJ', 'ibge': '3304557', 'endereco_id': 1, 'cliente_id': 1}]}]

def test_read_customer():
    response = client.get("/search-customer/1")
    assert response.status_code == 200
    assert response.json() == {'razao_social': 'Sol Eterno', 'email': 'atendimento@soleterno.com', 'nome_fantasia': 'Sol Eterno LTDA', 'telefone': '(21) 98207-9901', 'cpf': None, 'cnpj': '16.470.954/0001-06', 'cliente_id': 1, 'enderecos': [{'cep': '22783-115', 'logradouro': 'Estrada dos Bandeirantes', 'complemento': 'de 7995 a 8901 - lado ímpar', 'bairro': 'Jacarepaguá', 'localidade': 'Rio de Janeiro', 'uf': 'RJ', 'ibge': '3304557', 'endereco_id': 1, 'cliente_id': 1}]}
