from abc import ABC, abstractmethod
from typing import List, Dict

from app.application.dtos.parceiro_dto import ParceiroDto


class AbstractImportCsvUseCase(ABC):
    @abstractmethod
    async def execute(self, csv_content: str) -> Dict[str, List[ParceiroDto]]:
        """Process the given CSV content to update or create Parceiros"""
        pass
