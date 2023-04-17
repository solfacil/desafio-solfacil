from abc import ABC, abstractmethod
from typing import TypedDict


class Address(TypedDict):
    """Class to address representation"""

    uf: str | None
    city: str | None


class AddressApi(ABC):
    """Interface to AddressApi use case"""

    @abstractmethod
    def handle(self, cep: str) -> Address:
        """Case"""

        raise Exception("Should implement method: handle")
