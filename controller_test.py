import pytest
from run import app
from app import TestingConfig

@pytest.fixture
def client():
    app.config.from_object(TestingConfig)
    with app.test_client() as client:
        yield client

def test_upload_empty_csv(client):
    with open('empty_example.csv', 'rb') as file:
        response = client.post('/upload_partner', data={'file': file})
        assert response.status_code == 200
        assert response.json['data'] == []

def test_upload_invalid_field_csv(client):
    with open('invalid_field_example.csv', 'rb') as file:
        response = client.post('/upload_partner', data={'file': file})
        assert response.status_code == 200
        assert response.json['data'] == []

def test_upload_csv(client):
    with open('example.csv', 'rb') as file:
        response = client.post('/upload_partner', data={'file': file})
        assert response.status_code == 200
        assert response.json['data'] is not []
