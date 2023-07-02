from src.domain.models.address.model import PartnerModel
from src.infrastructures.postgres.infrastructure import PostgresInfrastructure

class PartnersRepository:

    async_session = PostgresInfrastructure.async_session

    @classmethod
    async def create_new_partner(cls, partner: PartnerModel):
        async with cls.async_session() as session:
            session.add(partner)
            await session.commit()


# from asyncio import run
#
#
# new_partner = PartnerModel(cnpj="teste", company_name="teste", fantasy_name="teste", phone="teste", email="teste"
#
# )
#
# a = run(PartnersRepository.create_new_partner(partner=new_partner))
