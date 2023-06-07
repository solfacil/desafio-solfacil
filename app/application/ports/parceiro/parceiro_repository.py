from abc import ABC, abstractmethod
from typing import List, Optional

from app.application.dtos.parceiro_dto import ParceiroDto
from app.domain.entities.parceiro.parceiro import Parceiro


class AbstractParceiroRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[ParceiroDto]:
        pass

    @abstractmethod
    def get_by_id(self, parceiro_id: int) -> Optional[ParceiroDto]:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[ParceiroDto]:
        pass

    @abstractmethod
    def add(self, parceiro: Parceiro) -> ParceiroDto:
        pass

    @abstractmethod
    def delete(self, parceiro_id: int) -> None:
        pass

    @abstractmethod
    def update(self, parceiro: Parceiro) -> ParceiroDto:
        pass

    @abstractmethod
    def get_by_cnpj(self, cnpj: str) -> ParceiroDto:
        pass

    @abstractmethod
    def begin_transaction(self):
        pass
