from asyncio import run

from src.infrastructures.postgres.infrastructure import PostgresInfrastructure

run(PostgresInfrastructure.create_tables())