from abc import ABC, abstractmethod
from typing import List

from .partner_dto import PartnerDto


class PartnerStorage(ABC):
    """Interface to PartnerStorage use case"""

    @abstractmethod
    def save_or_update_partner(self, partner_dto: PartnerDto):
        """Case"""

        raise Exception("Should implement method: save or update")

    @abstractmethod
    def get_all_partners(self) -> List[PartnerDto]:
        """Case"""

        raise Exception("Should implement method: get all")
