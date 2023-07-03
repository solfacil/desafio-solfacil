from typing import Union, List

import loglifos
from sqlalchemy import select

from src.domain.models.partners.model import PartnerModel
from src.domain.models.address.model import AddressModel
from src.infrastructures.postgres.infrastructure import PostgresInfrastructure

class PartnersRepository:

    async_session = PostgresInfrastructure.async_session

    @classmethod
    async def upsert_partner(cls, partner: PartnerModel):
        async with cls.async_session() as session:
            try:
                await session.merge(partner)
                await session.commit()

            except Exception as ex:
                loglifos.error(msg="Unexpected error", exception=ex)
                await session.rollback()

    @classmethod
    async def get_all_partners(cls) -> List[PartnerModel]:
        async with cls.async_session() as session:
            statement = select(PartnerModel)
            result = await session.execute(statement)
            all_partners = result.scalars().all()
            return all_partners



    @classmethod
    async def insert_one(cls, object_model: Union[PartnerModel, AddressModel]):
        async with cls.async_session() as session:
            session.add(object_model)
            await session.commit()


from asyncio import run
# new_partner = PartnerModel(
#     cnpj="1231231231231", phone="12311231", company_name="empresa_do_igor", fantasy_name="empresinha", email="teste@teste", zipcode="03718090")
# address_2 = AddressModel(address="blabla", complement="blabla2", neighborhood="teste", city="teste", state="SP", partner_id=2)
# adress_teste = AddressModel(address="blabla", complement="blabla2", neighborhood="teste", city="teste", state="SP", partner_id=1)
# a = run(PartnersRepository.insert_one(new_partner))
# run(PartnersRepository.insert_one(address_2))