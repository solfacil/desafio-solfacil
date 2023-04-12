


from api.models import Endereco, Parceiro


class ParceiroRepository(object):

    @staticmethod
    def save_partner(partner_obj: dict):
        from api.utils import clean_data_values

        cnpj = clean_data_values(partner_obj['cnpj'], '.,-/')
        cep =  clean_data_values(partner_obj['cep'], '-')
        telefone = clean_data_values(partner_obj['telefone'], '()  -')
        parceiro_exist = Parceiro.objects.filter(cnpj=cnpj).first()
        if parceiro_exist:
            parceiro_exist.razao_social = partner_obj['razao_social']
            parceiro_exist.nome_fantasia = partner_obj['nome_fantasia']
            parceiro_exist.telefone = telefone
            parceiro_exist.email = partner_obj['email']
            parceiro_exist.cep = cep
            parceiro_exist.save()
            ParceiroRepository.save_address(cep, parceiro_exist.id)
        else:
            Parceiro.objects.create(
                cnpj=cnpj,
                razao_social=partner_obj['razao_social'],
                nome_fantasia=partner_obj['nome_fantasia'],
                telefone=telefone,
                email=partner_obj['email'],
                cep=cep
            )
            partner = Parceiro.objects.filter(cnpj=cnpj).first()
            save_address = ParceiroRepository.save_address(cep, partner.id)
            if not save_address:
                return Exception('Erro ao salvar endereço')


    @staticmethod
    def save_address(cep, partner_id):
        from api.utils import get_address_by_cep

        try:
            address = get_address_by_cep(cep)
        except Exception:
            return False
    
        partner_with_address = Endereco.objects.filter(parceiro_id=partner_id).first()
        if partner_with_address:
            partner_with_address.logradouro = address['logradouro']
            partner_with_address.complemento = address['complemento']
            partner_with_address.bairro = address['bairro']
            partner_with_address.cidade = address['localidade']
            partner_with_address.estado = address['uf']
            partner_with_address.save()
        else:
            if address:
                Endereco.objects.create(
                    parceiro_id=partner_id,
                    cep=cep,
                    logradouro=address['logradouro'],
                    complemento=address['complemento'],
                    bairro=address['bairro'],
                    cidade=address['localidade'],
                    estado=address['uf']
                )
        return True
            