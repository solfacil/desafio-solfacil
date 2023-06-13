import requests
import json

CEP_API = "https://viacep.com.br/ws/"

def get_url(cep):
    return CEP_API + cep + "/json/"

def request_cep(cep):
    url = get_url(cep)
    r = requests.get(url)
    cep_response = json.loads(r.text)
    return cep_response
