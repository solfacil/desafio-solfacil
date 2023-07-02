from decouple import config
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.pool import NullPool

from src.domain.models.orm_base.model import Base


class PostgresInfrastructure:

    async_engine = create_async_engine(
        config("POSTGRES_URL"), echo=True, poolclass=NullPool, pool_pre_ping=True
    )
    async_session = async_sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)


    @classmethod
    async def create_tables(cls):
        async with cls.async_engine.begin() as conn:
            # await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)


# from asyncio import run
# new_partner = PartnerModel(cnpj="teste", company_name="teste", fantasy_name="teste", phone="teste", email="teste"
#
# )
# a = run(PostgresInfrastructure.create_new_partner(partner=new_partner))
# a = run(PostgresInfrastructure.create_tables())
