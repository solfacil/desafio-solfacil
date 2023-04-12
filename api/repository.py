


from api.models import Endereco, Parceiro


class ParceiroRepository(object):

    @staticmethod
    def save_partner(row: dict):
        from api.utils import clean_data_values

        cnpj = clean_data_values(row['cnpj'], '.,-/')
        cep =  clean_data_values(row['cep'], '-')
        telefone = clean_data_values(row['telefone'], '()  -')
        parceiro_exist = Parceiro.objects.filter(cnpj=cnpj).first()
        if parceiro_exist:
            parceiro_exist.razao_social = row['razao_social']
            parceiro_exist.nome_fantasia = row['nome_fantasia']
            parceiro_exist.telefone = telefone
            parceiro_exist.email = row['email']
            parceiro_exist.cep = cep
            parceiro_exist.save()
            ParceiroRepository.save_address(cep, parceiro_exist.id)
        else:
            Parceiro.objects.create(
                cnpj=cnpj,
                razao_social=row['razao_social'],
                nome_fantasia=row['nome_fantasia'],
                telefone=telefone,
                email=row['email'],
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
    
        address_exist = Endereco.objects.filter(cep=cep, parceiro_id=partner_id).first()
        if address_exist:
            address_exist.logradouro = address['logradouro']
            address_exist.complemento = address['complemento']
            address_exist.bairro = address['bairro']
            address_exist.cidade = address['localidade']
            address_exist.estado = address['uf']
            address_exist.save()
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
            