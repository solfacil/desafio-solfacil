import csv
import io
import re
import unicodedata

from api.validators import (validate_cep, validate_cnpj, validate_razao_social,
                            validate_telefone)


def process_csv_file(csv_file):
    """
        Processa um arquivo CSV e retorna um gerador de objetos normalizados.

        Args:
            csv_file (File): Arquivo CSV contendo os dados dos parceiros.

        Yields:
            dict: Objeto parceiro normalizado.
    """
    with io.StringIO(csv_file.read().decode()) as csvfile:
        csv_file_reader = csv.DictReader(csvfile)
        for partner_obj in csv_file_reader:
            normalized_partner_obj = normalize_key_object(partner_obj)
            validate_errors = validate_fields_partner(normalized_partner_obj)
            if not validate_errors:
                yield normalized_partner_obj
                

def process_and_save_csv_values(csv_file,parceiro_repository):
    """
        Processa um arquivo CSV e salva os dados no banco de dados.

        Args:
            csv_file (File): Arquivo CSV contendo os dados dos parceiros.
            parceiro_repository (ParceiroRepository): Objeto de repositório de parceiros.
    """
    partner_objs = process_csv_file(csv_file)
    for partner_obj in partner_objs:
        parceiro_repository.save_partner(partner_obj)


def normalize_key_object(dict_obj):
    """
        Normaliza as chaves de um dicionário.

        Args:
            dict_obj (dict): Dicionário com as chaves a serem normalizadas.

        Returns:
            dict: Dicionário com as chaves normalizadas.
    """
    normalized_dict = {}
    for key, value in dict_obj.items():
        normalized_key = re.sub(r'[./()\-\s]', '', key).lower()
        normalized_key = unicodedata.normalize('NFKD', normalized_key).encode(
            'ASCII', 'ignore').decode('ASCII')
        if normalized_key == 'razaosocial':
            normalized_key =  'razao_social'
        elif normalized_key == 'nomefantasia':
            normalized_key = 'nome_fantasia'
        normalized_dict[normalized_key] = value
    return normalized_dict


def validate_fields_partner(partner_obj):
    """
        Valida os campos de um objeto parceiro.

        Args:
            partner_obj (dict): Objeto parceiro a ser validado.
    
    """
    cnpj = clean_data_values(partner_obj['cnpj'], '.,-/')
    cep = clean_data_values(partner_obj['cep'], '-')
    telefone = clean_data_values(partner_obj['telefone'], '()  -')
    validate_cnpj(cnpj)
    validate_cep(cep)
    validate_telefone(telefone)
    validate_razao_social(partner_obj['razao_social'])


def clean_data_values(value, character):
    """
        Remove caracteres de um valor.

        Args:
            value (str): Valor a ser limpo.
            character (str): String com os caracteres a serem removidos.

        Returns:
            str: Valor limpo.
    """
    for char in character:
        value = value.replace(char, '')
    return value

