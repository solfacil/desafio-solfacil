import csv
import io
import json

import requests

from api.models import Parceiro
from api.repository import ParceiroRepository


# Função que é chamada na migration para popular a tabela com o CSV dentro do projeto
def populate_partners_csv(apps, schema_editor):
    with open('parceiros.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            parceiro = Parceiro.objects.create(
                cnpj=row['cnpj'],
                razao_social=row['razao_social'],
                nome_fantasia=row['nome_fantasia'],
                telefone=row['telefone'],
                email=row['email'],
                cep=row['cep']
            )
            parceiro.save()

# Função que vai ser acionada quando batermos no endpoint de parceiros_csv
def process_and_save_csv_values(csv_file):
    with io.StringIO(csv_file.read().decode()) as csvfile:
        reader = csv.DictReader(csvfile)
        errors = {}
        for row in reader:
            validate_errors = validate_fields_partner(row)
            if validate_errors:
                errors.update(validate_errors)
            else:
               ParceiroRepository.save_partner(row)
    
        return errors or None

#função utilizada para validar os campos do parceiro
def validate_fields_partner(row):
    errors = {}

    cnpj = clean_data_values(row['cnpj'], '.,-/')
    cep =  clean_data_values(row['cep'], '-')
    telefone = clean_data_values(row['telefone'], '()  -')

    if len(cnpj) != 14 or not cnpj.isdigit():
        errors['cnpj'] = 'CNPJ inválido'
    elif not cnpj:
        errors['cnpj'] = 'Necessário ter um CNPJ.'
    if len(cep) != 8 or not cep.isdigit():
        errors['cep'] = 'CEP inválido'
    if len(telefone) != 11 or not telefone.isdigit():
        errors['telefone'] = 'Telefone inválido'
    if not row['razao_social']:
        errors['razao_social'] = 'Necessário ter uma razão social'
    if errors:
        errors['Errors'] = 'Foram encontrados {} objetos com erro durante o processo de adicionar valores'.format(len(errors))

    return errors or None

# função utilizada para limpar os caracteres especiais dos campos
def clean_data_values(value, character):
    for char in character:
        value = value.replace(char, '')
    return value

# função utilizada para buscar os dados do cep
def get_address_by_cep(cep):
    # cep = clean_data_values(cep, '-')
    url = 'https://viacep.com.br/ws/{}/json/'.format(cep)
    response = requests.get(url)
    content =  response.content.decode('utf-8')
    address = json.loads(content)
    if 'erro' in address:
        return None
    
    return address