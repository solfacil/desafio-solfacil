import json

import requests

from api.application.partner import AddressApi


class PartnerAddressApi(AddressApi):
    def handle(self, cep: str):
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)

        if response.status_code == 400:
            return {"uf": None, "city": None}
        else:
            content = response.content.decode("utf-8")
            address = json.loads(content)
            return {
                "uf": address["uf"],
                "city": address["localidade"],
            }
