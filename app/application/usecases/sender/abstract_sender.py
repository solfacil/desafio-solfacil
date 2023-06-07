from abc import ABC, abstractmethod


class AbstractSender(ABC):

    @abstractmethod
    async def send(self, recipient: str, subject: str, body: str) -> None:
        pass
