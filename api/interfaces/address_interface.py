import json
import os

import requests


class AddressInterface:
    def __init__(self, cache_path=None):
        self.cache_path = cache_path or os.path.join(os.getcwd(), 'address_cache.json')
        self.cache = {}

    def get_address(self, cep):
        if cep in self.cache:
            return self.cache[cep]

        url = 'https://viacep.com.br/ws/{}/json/'.format(cep)
        response = requests.get(url)
        content = response.content.decode('utf-8')
        address = json.loads(content)

        if 'erro' in address:
            if cep in self.cache:
                return self.cache[cep]
            else:
                return None

        self.cache[cep] = address

        with open(self.cache_path, 'w') as f:
            json.dump(self.cache, f)

        return address