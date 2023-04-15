import requests

from api.interfaces.address_interface import AddressInterface
from api.models import Endereco, Parceiro
from api.utils import clean_data_values, validate_fields_partner


class ParceiroRepository():

    @staticmethod
    def save_partner(partner_obj: dict):
        validate_fields_partner(partner_obj)

        cnpj = clean_data_values(partner_obj['cnpj'], '.,-/')
        cep =  clean_data_values(partner_obj['cep'], '-')
        telefone = clean_data_values(partner_obj['telefone'], '()  -')
        
        partner_existent = Parceiro.objects.filter(cnpj=cnpj).first()
        if partner_existent is not None:
            partner_updated = ParceiroRepository.update_partner(partner_obj, cep, telefone, partner_existent)
            partner_updated.save()
            ParceiroRepository.save_address(cep, partner_existent.id)
        else:
            partner = ParceiroRepository.new_partner(partner_obj, cep, telefone, cnpj)
            partner.save()
            ParceiroRepository.save_address(cep, partner.id)

  
    @staticmethod   
    def save_address(cep, partner_id):
        try:
            address_finder = AddressInterface()
            address = address_finder.get_address(cep)
        except requests.exceptions.RequestException as e:
            raise Exception(f'Erro ao buscar endereço por: {e}')
        if address:
            partner_with_address = Endereco.objects.filter(parceiro_id=partner_id).first()
            if partner_with_address is not None:
                address_updated = ParceiroRepository.update_address(partner_with_address, address)
                address_updated.save()
            else:
                address_new = ParceiroRepository.new_address(address, partner_id,cep)
                address_new.save()


    def update_partner(partner_obj, cep, telefone, partner_existent=None):
        try:
            partner = partner_existent
            partner.razao_social = partner_obj['razao_social']
            partner.nome_fantasia = partner_obj['nome_fantasia']
            partner.telefone = telefone
            partner.email = partner_obj['email']
            partner.cep = cep

            return partner
        except KeyError as e:
            raise Exception(f'Erro ao criar parceiro por: {e}')


    def new_partner(partner_obj, cep, telefone, cnpj):
        try:
            partner = Parceiro()
            partner.cnpj = cnpj
            partner.razao_social = partner_obj['razao_social']
            partner.nome_fantasia = partner_obj['nome_fantasia']
            partner.telefone = telefone
            partner.email = partner_obj['email']
            partner.cep = cep

            return partner
        except KeyError as e:
            raise Exception(f'Erro ao criar parceiro por: {e}')


    def update_address(partner_with_address, address):
        try:
            partner_with_address.logradouro = address['logradouro']
            partner_with_address.complemento = address['complemento']
            partner_with_address.bairro = address['bairro']
            partner_with_address.cidade = address['localidade']
            partner_with_address.estado = address['uf']
            partner_with_address.save()
            return partner_with_address
        except KeyError as e:
            raise Exception(f'Erro ao criar endereço por: {e}')
    

    def new_address(address, partner_id,cep):
        try:
            partner_address = Endereco()
            partner_address.cep = cep
            partner_address.logradouro = address['logradouro']
            partner_address.complemento = address['complemento']
            partner_address.bairro = address['bairro']
            partner_address.cidade = address['localidade']
            partner_address.estado = address['uf']
            partner_address.parceiro_id = partner_id
            partner_address.save()
            return partner_address
        except KeyError as e:
            raise Exception(f'Erro ao criar endereço por: {e}')