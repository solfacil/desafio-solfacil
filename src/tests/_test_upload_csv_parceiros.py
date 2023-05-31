import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from desafio_solfacil.src.domains.parceiros.repositories.sqlalchemy.models import (
    Parceiro,
)

from ..routes_v1 import router

app = FastAPI(
    title="Atualização em lote de Parceiros",
    description="Endpoints para listagem e atualização de parceiros em lote através de arquivo csv",
)

app.include_router(router, prefix="/parceiros")

client = TestClient(app)


class TestUploadCsvParceiros:
    # Tests uploading a valid CSV file with valid data.
    @pytest.mark.asyncio
    async def test_upload_csv_valid_file(self, mocker):
        # Mock the read_csv function to return valid data
        mocker.patch(
            "desafio_solfacil.src.utils.read_file.read_csv",
            return_value=[
                {
                    "CNPJ": "12345678901234",
                    "Razão Social": "Empresa A",
                    "Nome Fantasia": "Empresa A",
                    "Telefone": "1234567890",
                    "Email": "empresaA@test.com",
                    "CEP": "12345678",
                },
                {
                    "CNPJ": "23456789012345",
                    "Razão Social": "Empresa B",
                    "Nome Fantasia": "Empresa B",
                    "Telefone": "2345678901",
                    "Email": "empresaB@test.com",
                    "CEP": "23456789",
                },
            ],
        )

        # Mock the define_parceiro_location function to return valid data
        mocker.patch(
            "desafio_solfacil.src.utils.cep_search.define_parceiro_location",
            return_value={"cidade": "São Paulo", "estado": "SP"},
        )

        # Mock the is_cnpj_valid function to always return True
        mocker.patch(
            "desafio_solfacil.src.utils.validations.is_cnpj_valid", return_value=True
        )

        # Mock the is_email_valid function to always return True
        mocker.patch(
            "desafio_solfacil.src.utils.validations.is_email_valid", return_value=True
        )

        # Mock the create_parceiro function to always return a Parceiro object
        mocker.patch(
            "desafio_solfacil.src.domains.parceiros.repositories.sqlalchemy.crud.create_parceiro",
            return_value=Parceiro(),
        )

        # Mock the send_email function to do nothing
        mocker.patch("desafio_solfacil.src.utils.write_notification.send_email")

        # Make a POST request with a valid CSV file
        with open("./assets/valid_parceiros.csv", mode="rb") as file:
            response = client.post("/parceiros/upload_csv/", files={"file": file})

        # Check that the response is successful and there are no errors
        assert response.status_code == 200
        assert response.json() == {
            "message": "CSV file uploaded successfully.",
            "errors": [],
        }

    # Tests uploading a valid CSV file with some invalid data.
    @pytest.mark.asyncio
    async def test_upload_csv_invalid_data(self, mocker):
        # Mock the read_csv function to return invalid data
        mocker.patch(
            "desafio_solfacil.src.utils.read_file.read_csv",
            return_value=[
                {
                    "CNPJ": "12345678901234",
                    "Razão Social": "Empresa A",
                    "Nome Fantasia": "Empresa A",
                    "Telefone": "1234567890",
                    "Email": "empresaA@test.com",
                    "CEP": "12345678",
                },
                {
                    "CNPJ": "23456789012345",
                    "Razão Social": "",
                    "Nome Fantasia": "",
                    "Telefone": "",
                    "Email": "empresaB@test.com",
                    "CEP": "",
                },
            ],
        )

        # Mock the define_parceiro_location function to return valid data
        mocker.patch(
            "desafio_solfacil.src.utils.cep_search.define_parceiro_location",
            return_value={"cidade": "São Paulo", "estado": "SP"},
        )

        # Mock the is_cnpj_valid function to always return True
        mocker.patch(
            "desafio_solfacil.src.utils.validations.is_cnpj_valid", return_value=True
        )

        # Mock the is_email_valid function to always return True
        mocker.patch(
            "desafio_solfacil.src.utils.validations.is_email_valid", return_value=True
        )

        # Mock the create_parceiro function to always return a Parceiro object
        mocker.patch(
            "desafio_solfacil.src.domains.parceiros.repositories.sqlalchemy.crud.create_parceiro",
            return_value=Parceiro(),
        )

        # Mock the send_email function to do nothing
        mocker.patch("desafio_solfacil.src.utils.write_notification.send_email")

        # Make a POST request with an invalid CSV file
        with open("./assets/invalid_parceiros.csv", mode="rb") as file:
            response = client.post("/parceiros/upload_csv/", files={"file": file})

        # Check that the response is successful and there are errors
        assert response.status_code == 200
        assert response.json() == {
            "message": "CSV file uploaded successfully.",
            "errors": [
                "Erro na linha 2. Razão Social inválido! Contate o parceiro e valide a informação 1234567890",  # noqa
                "Erro na linha 2. Nome Fantasia inválido! Contate o parceiro e valide a informação 1234567890",  # noqa
                "Erro na linha 2. CEP inválido! Contate o parceiro e valide a informação 1234567890",   # noqa
            ],
        }
