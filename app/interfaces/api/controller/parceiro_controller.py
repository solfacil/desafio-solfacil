from typing import List, Dict

from app.application.dtos.parceiro_dto import ParceiroDto
from app.application.ports.parceiro.parceiro_repository import AbstractParceiroRepository
from app.application.usecases.parceiro.abstract_import_csv import AbstractImportCsvUseCase
from app.domain.usecases.parceiro.import_csv import ImportCsvUseCase
from app.infrastructure.database.sqlalchemy.sql_parceiro_repository import SqlAlchemyParceiroRepository


class ParceiroController:
    def __init__(
            self,
            repo: AbstractParceiroRepository,
            usecase: AbstractImportCsvUseCase,
    ):
        self.repo = repo
        self.usecase = usecase

    async def get_all_parceiros(self) -> List[ParceiroDto]:
        return self.repo.get_all()

    async def upload_csv(self, csv_file: str) -> Dict[str, List[ParceiroDto]]:
        parceiros_updated_created: Dict[str, List[ParceiroDto]] = await self.usecase.execute(
            csv_file,
        )
        return parceiros_updated_created

async def get_controller() -> ParceiroController:
    parceiro_repository = SqlAlchemyParceiroRepository()
    return ParceiroController(
        repo=SqlAlchemyParceiroRepository(),
        usecase=ImportCsvUseCase(parceiro_repository),
    )
