import csv
import io
import json
import re
import unicodedata

import requests

from api.repository import ParceiroRepository


def process_and_save_csv_values(csv_file):
    with io.StringIO(csv_file.read().decode()) as csvfile:
        csv_file_reader = csv.DictReader(csvfile)
        errors = {}
        for partner_obj in csv_file_reader:
            normalized_partner_obj = normalize_fieldname(partner_obj)
            validate_errors = validate_fields_partner(normalized_partner_obj)
            if validate_errors:
                errors.update(validate_errors)
            else:
                ParceiroRepository.save_partner(normalized_partner_obj)

        return errors or None


def validate_fields_partner(partner_obj):
    errors = {}

    cnpj = clean_data_values(partner_obj['cnpj'], '.,-/')
    cep = clean_data_values(partner_obj['cep'], '-')
    telefone = clean_data_values(partner_obj['telefone'], '()  -')

    if len(cnpj) != 14 or not cnpj.isdigit():
        errors['cnpj'] = 'CNPJ inválido'
    elif not cnpj:
        errors['cnpj'] = 'Necessário ter um CNPJ.'
    if len(cep) != 8 or not cep.isdigit():
        errors['cep'] = 'CEP inválido'
    if len(telefone) != 11 or not telefone.isdigit():
        errors['telefone'] = 'Telefone inválido'
    if not partner_obj['razao_social']:
        errors['razao_social'] = 'Necessário ter uma razão social'
    if errors:
        errors['Errors'] = 'Foram encontrados {} objetos com erro durante o processo de adicionar valores'.format(
            len(errors))

    return errors or None


def clean_data_values(value, character):
    for char in character:
        value = value.replace(char, '')
    return value


def get_address_by_cep(cep):
    url = 'https://viacep.com.br/ws/{}/json/'.format(cep)
    response = requests.get(url)
    content = response.content.decode('utf-8')
    address = json.loads(content)

    if 'erro' in address:
        return None

    return address


def normalize_fieldname(dict_obj):
    normalized_dict = {}
    for key, value in dict_obj.items():
        normalized_key = re.sub(r'[./()\-\s]', '', key).lower()
        normalized_key = unicodedata.normalize('NFKD', normalized_key).encode('ASCII', 'ignore').decode('ASCII')
        if normalized_key == 'razaosocial':
            normalized_key =  'razao_social'
        elif normalized_key == 'nomefantasia':
            normalized_key = 'nome_fantasia'
        normalized_dict[normalized_key] = value
    return normalized_dict

        