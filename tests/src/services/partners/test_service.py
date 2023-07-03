from unittest.mock import patch

import pytest

from domain.models.partners.model import PartnerModel
from src.services.partners.service import PartnersService


@pytest.mark.asyncio
@patch('src.services.partners.service.PartnersRepository.upsert_partner')
async def test_when_valid_file_then_upload_with_successfully(mock_repo, upload_file):
    result = await PartnersService.load_from_csv_file(file=upload_file)

    assert isinstance(result, str)
    assert result == f"{upload_file.filename} uploaded successfully."


@pytest.mark.asyncio
async def test_when_valid_spooled_file_then_get_partners_model(partners_df):

    result = await PartnersService.get_partner_model_list(partners_df=partners_df)

    assert isinstance(result, list)
    assert result[0].cnpj == '16470954000106'
    assert result[0].email == "atendimento@soleterno.com"