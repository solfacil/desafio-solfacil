import re
import requests
from .logger import Logger

logger = Logger(__file__)

CEP_URL = 'https://viacep.com.br/ws/$CEP_PARCEIRO$/json/'

class Utils:
    @staticmethod
    def check_cnpj(cnpj):
        pattern = r"[0-9]{2}\.?[0-9]{3}\.?[0-9]{3}\/?[0-9]{4}\-?[0-9]{2}"
        if re.match(pattern, cnpj):
            return True
        else:
            return False
    
    @staticmethod
    def check_email(email):
        pattern = r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$"
        if re.match(pattern, email):
            return True
        else:
            return False
        
    @staticmethod
    def check_telefone(telefone):
        pattern = r"(\(\d{2}\)\s)(\d{4,5}\-\d{4})"
        if re.match(pattern, telefone):
            return True
        else:
            return False
        
    @staticmethod
    def get_address_by_cep(cep):
        logger.info('Verificando cep...')
        logger.info(f'cep: {cep}')

        url = CEP_URL.replace("$CEP_PARCEIRO$", cep)
        logger.info(f'url: {url}')
        req = requests.get(url)

        if req.status_code != 400:
            logger.info(f'req.status_code: {req.status_code}')
            address = req.json()
            logger.info(f'address: {address}')
            return address

        return None
              