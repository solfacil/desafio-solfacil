from unittest.mock import AsyncMock

import pandas as pd
import pytest
from pytest_mock import MockerFixture

from app.application.dtos.parceiro_dto import ParceiroDto
from app.application.ports.parceiro.parceiro_repository import AbstractParceiroRepository
from app.domain.entities.parceiro.parceiro import Parceiro
from app.domain.usecases.parceiro.import_csv import ImportCsvUseCase

csv_content = """CNPJ,Razão Social,Nome Fantasia,Telefone,Email,CEP\n16.470.954/0001-06,Sol Eterno,Sol Eterno LTDA,(21) 98207-9901,atendimento@soleterno.com,22783-115"""

df = pd.DataFrame({
    "CNPJ": ["16470954000106"],
    "Razão Social": ["Sol Eterno"],
    "Nome Fantasia": ["Sol Eterno LTDA"],
    "Telefone": ["21982079901"],
    "Email": ["atendimento@soleterno.com"],
    "CEP": ["22783115"],
    "Cidade": ["Rio de Janeiro"],
    "Estado": ["RJ"],
})

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
async def test_import_csv(mocker: MockerFixture):

    # Mock
    parceiro_repository = mocker.MagicMock(AbstractParceiroRepository)
    parceiro_repository.get_by_cnpj = mocker.MagicMock(return_value=parceiro)
    parceiro_repository.add = mocker.MagicMock(return_value=parceiro_dto)
    parceiro_repository.update = mocker.MagicMock(return_value=parceiro_dto)

    mocker.patch(
        "app.domain.usecases.email_sender.email_sender.EmailSender.send",
        new_callable=AsyncMock, return_value=None,
    )

    mocker.patch(
        "app.infrastructure.integrations.via_cep.ViaCep.get_address",
        new_callable=AsyncMock, return_value={
            "cidade": "Rio de Janeiro", "estado": "RJ",
        },
    )

    # Act
    use_case = ImportCsvUseCase(parceiro_repository)
    result = await use_case.execute(csv_content)

    # Assert
    parceiro_repository.get_by_cnpj.assert_called_with("16470954000106")
    parceiro_repository.add.assert_called_with(parceiro)
    expected_result = {"created": [parceiro_dto], "updated": []}
    assert result == expected_result
