from asyncio import run

from src.infrastructures.postgres.infrastructure import PostgresInfrastructure
from src.domain.models.partners.model import PartnerModel
from src.domain.models.address.model import AddressModel

run(PostgresInfrastructure.create_tables())