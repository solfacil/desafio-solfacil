# from fastapi import UploadFile
from typing import List

from starlette.datastructures import UploadFile

from src.domain.models.partners.model import PartnerModel
from src.domain.validators.response.partners.validator import PartnersResponse
from src.repositories.postgres.repository import PartnersRepository
from src.services.data_frame.service import DataFrameService


class PartnersService:
    @classmethod
    async def load_from_csv_file(cls, file: UploadFile) -> str:
        partners_df = await DataFrameService.convert_csv_to_df(spooled_file=file.file)
        partner_model_list = await cls.get_partner_model_list(partners_df=partners_df)
        for partner in partner_model_list:
            await PartnersRepository.upsert_partner(partner=partner)

        return f"{file.filename} uploaded successfully."

    @staticmethod
    async def get_partner_model_list(partners_df) -> List[PartnerModel]:
        partner_model_list = [
            PartnerModel(**row.to_dict()) for index, row in partners_df.iterrows()
        ]
        return partner_model_list

    @staticmethod
    async def get_all_partners() -> List[dict]:
        all_partners = await PartnersRepository.get_all_partners()
        partners_validated = [
            PartnersResponse(**partner.__dict__).dict() for partner in all_partners
        ]
        return partners_validated
