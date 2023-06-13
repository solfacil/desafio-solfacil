import re

def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if(re.fullmatch(regex, email)):
        return True
    return False

def validate_cnpj(cnpj):
    cnpj = parse_cnpj(cnpj)
    if len(cnpj) == 14:
        return True
    return False

def parse_cnpj(cnpj):
    return cnpj.replace('.', '').replace('/', '').replace('-', '')

def parse_phone(phone):
    return phone.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
