import re

import requests


class ViaCepApi:
    def __init__(self):
        self.base_url = "https://viacep.com.br/ws/"

    def get_address(self, cep):
        cep = self.clear_cep(cep)
        response = requests.get(self.base_url + cep + "/json/")

        if response.status_code == 200:
            return response.json()
        else:
            return False

    @staticmethod
    def clear_cep(cep):
        return re.sub(r"[^0-9]", "", cep)
