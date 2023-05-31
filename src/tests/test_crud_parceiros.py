from uuid import uuid4

import pytest

from ..domains.parceiros.repositories.sqlalchemy.crud import (
    create_parceiro,
    get_parceiro_by_cnpj,
    update_parceiro,
)
from ..domains.parceiros.repositories.sqlalchemy.models import Parceiro
from ..routes_v1 import fetch_all_parceiros


class TestCrudParceiros:
    @pytest.mark.asyncio
    async def test_create_parceiro_invalid_cnpj(self, mocker):
        # Arrange
        db_mock = mocker.Mock()
        parceiro_mock = {"cnpj": "12345678901234"}

        # Act and Assert
        with pytest.raises(Exception):
            await create_parceiro(db=db_mock, parceiro=parceiro_mock)

    # Tests that the function creates a new partner and returns it.

    @pytest.mark.asyncio
    async def test_create_parceiro(self, mocker):
        # Arrange
        db_mock = mocker.Mock()
        parceiro_mock = {
            "cnpj": "16.470.954/0001-06",
            "razao_social": "Empresa",
            "nome_fantasia": "Empresa Fantasia",
            "telefone": "1234567890",
            "email": "empresa@empresa.com",
            "cidade": "Cidade",
            "estado": "Estado",
            "cep": "12345678",
        }
        db_parceiro_mock = Parceiro(id_=uuid4(), **parceiro_mock)
        db_mock.add.return_value = None
        db_mock.commit.return_value = None
        db_mock.refresh.return_value = None
        db_mock.query.return_value.get.return_value = db_parceiro_mock

        # Act
        result = create_parceiro(db=db_mock, parceiro=parceiro_mock)

        # Assert
        assert result.cnpj == db_parceiro_mock.cnpj

    # Tests that the function updates an existing partner and returns it.

    @pytest.mark.asyncio
    async def test_update_parceiro(self, mocker):
        # Arrange
        db_mock = mocker.Mock()
        parceiro_mock = {
            "cnpj": "12345678901234",
            "razao_social": "Empresa",
            "nome_fantasia": "Empresa Fantasia",
            "telefone": "1234567890",
            "email": "empresa@empresa.com",
            "cidade": "Cidade",
            "estado": "Estado",
            "cep": "12345678",
        }
        updated_parceiro_data_mock = {
            "razao_social": "Nova Empresa",
            "nome_fantasia": "Nova Empresa Fantasia",
            "telefone": "0987654321",
            "email": "novaempresa@novaempresa.com",
            "cep": "87654321",
        }
        db_parceiro_mock = Parceiro(id_=uuid4(), **parceiro_mock)
        db_mock.commit.return_value = None
        db_mock.close.return_value = None

        # Act
        update_parceiro(
            db=db_mock,
            parceiro=db_parceiro_mock,
            updated_parceiro_data=updated_parceiro_data_mock,
        )

        # Assert
        assert (
            db_parceiro_mock.razao_social == updated_parceiro_data_mock["razao_social"]
        )
        assert (
            db_parceiro_mock.nome_fantasia
            == updated_parceiro_data_mock["nome_fantasia"]
        )
        assert db_parceiro_mock.telefone == updated_parceiro_data_mock["telefone"]
        assert db_parceiro_mock.email == updated_parceiro_data_mock["email"]
        assert db_parceiro_mock.cep == updated_parceiro_data_mock["cep"]

    # Tests that the function retrieves a partner by CNPJ and returns it.

    @pytest.mark.asyncio
    async def test_get_parceiro_by_cnpj(self, mocker):
        # Arrange
        db_mock = mocker.Mock()
        parceiro_mock = {
            "cnpj": "12345678901234",
            "razao_social": "Empresa",
            "nome_fantasia": "Empresa Fantasia",
            "telefone": "1234567890",
            "email": "empresa@empresa.com",
            "cidade": "Cidade",
            "estado": "Estado",
            "cep": "12345678",
        }
        db_parceiro_mock = Parceiro(id_=uuid4(), **parceiro_mock)
        db_mock.query.return_value.get.return_value = db_parceiro_mock

        # Act
        result = get_parceiro_by_cnpj(
            db=db_mock, Parceiro=Parceiro, parceiro=parceiro_mock
        )

        # Assert
        assert result == db_parceiro_mock

    @pytest.mark.asyncio
    async def test_fetch_all_parceiros_default_params(self, mocker):
        # Arrange
        db_mock = mocker.Mock()
        parceiros_mock = [
            Parceiro(
                id_=uuid4(),
                cnpj="12345678901234",
                razao_social="Empresa",
                nome_fantasia="Empresa Fantasia",
                telefone="1234567890",
                email="empresa@empresa.com",
                cidade="Cidade",
                estado="Estado",
                cep="12345678",
            )
        ]
        db_mock.query.return_value.offset.return_value.limit.return_value.all.return_value = (
            parceiros_mock
        )

        # Act
        result = await fetch_all_parceiros(db=db_mock)

        # Assert
        assert result == parceiros_mock
