import httpx
from typing import NewType
import logging

TCep = NewType("TCep", dict)


class ViaCep:
    def __init__(self, cep):
        self.cep = cep

    async def get_address(self):
        async with httpx.AsyncClient() as client:
            logging.info("Getting address from ViaCep")
            base_url = f"https://viacep.com.br/ws/{self.cep}/json/"
            response = await client.get(base_url)

            if response.status_code == 200:
                logging.info("Address found")
                data = response.json()
                return {
                    "cidade": data.get("localidade"),
                    "estado": data.get("uf")
                }
            logging.info("Address not found")
