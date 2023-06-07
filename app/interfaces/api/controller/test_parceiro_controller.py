import pytest
from unittest.mock import AsyncMock
from app.application.dtos.parceiro_dto import ParceiroDto
from app.application.ports.parceiro.parceiro_repository import AbstractParceiroRepository
from app.application.usecases.parceiro.abstract_import_csv import AbstractImportCsvUseCase
from app.domain.entities.parceiro.parceiro import Parceiro
from app.domain.usecases.parceiro.import_csv import ImportCsvUseCase
from app.infrastructure.database.sqlalchemy.sql_parceiro_repository import SqlAlchemyParceiroRepository
from app.interfaces.api.controller.parceiro_controller import ParceiroController

parceiro = Parceiro(
    cnpj="16470954000106",
    razao_social="Sol Eterno",
    nome_fantasia="Sol Eterno LTDA",
    telefone="21982079901",
    email="atendimento@soleterno.com",
    cep="22783115",
    cidade="Rio de Janeiro",
    estado="RJ",
)

parceiro_dto = ParceiroDto(**parceiro.dict())

@pytest.mark.asyncio
async def test_get_all_parceiros(mocker):
    # Arrange
    mock_repo = mocker.MagicMock(AbstractParceiroRepository)
    mock_usecase = mocker.MagicMock(AbstractImportCsvUseCase)
    controller = ParceiroController(repo=mock_repo, usecase=mock_usecase)
    expected = [parceiro_dto.dict()]
    mock_repo.get_all = mocker.MagicMock(return_value=expected)

    # Act
    result = await controller.get_all_parceiros()

    # Assert
    assert result == expected
    mock_repo.get_all.assert_called_once()

@pytest.mark.asyncio
async def test_upload_csv(mocker):
    # Arrange
    mock_repo = mocker.MagicMock(AbstractParceiroRepository)
    mock_usecase = mocker.MagicMock(AbstractImportCsvUseCase)
    controller = ParceiroController(repo=mock_repo, usecase=mock_usecase)
    csv_file = "test"
    expected = {"created": [parceiro_dto], "updated": [parceiro_dto]}
    mock_usecase.execute = AsyncMock(return_value=expected)

    # Act
    result = await controller.upload_csv(csv_file)

    # Assert
    assert result == expected
    mock_usecase.execute.assert_called_once_with(csv_file)
