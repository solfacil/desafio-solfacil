
from app.models.partner import Partner
from app.services.email import EmailService
from app import Utils, Logger
from multiprocessing import JoinableQueue

logger = Logger(__file__)

class PartnerService:
    @staticmethod
    def list_all_partners():
        return Partner.get_all()
    
    @staticmethod
    def valid_partner_values(data):
        valid_data = True

        cnpj = data[0]
        if not Utils.check_cnpj(cnpj):
            logger.info(f'Campo cnpj inválido: {cnpj}')
            valid_data = False
        
        razao_social = data[1]
        if not razao_social:
            logger.info(f'Campo razao_social inválido: {razao_social}')
            valid_data = False
        
        nome_fantasia = data[2]
        if not nome_fantasia:
            logger.info(f'Campo nome_fantasia inválido: {nome_fantasia}')
            valid_data = False
        
        telefone = data[3]
        if not Utils.check_telefone(telefone):
            logger.info(f'Campo telefone inválido: {telefone}')
            valid_data = False

        email = data[4]
        if not Utils.check_email(email):
            logger.info(f'Campo email inválido: {email}')
            valid_data = False
        
        cep = data[5]
        if not cep:
            logger.info(f'Campo cep inválido: {cep}')
            valid_data = False
        
        return valid_data
    
    @staticmethod
    def upload_csv_partner(data):
        csv_queue = JoinableQueue()
        for row in data:
            csv_queue.put(row)

        return PartnerService.thread_csv_partner_rows(csv_queue)
    
    @staticmethod
    def thread_csv_partner_rows(csv_queue):
        done_rows = 0
        rows_csv = csv_queue.qsize()
        logger.info(f'Quantidade de Parceiro para atualizar/salvar: {rows_csv}')
        resp = []

        while done_rows != rows_csv:
            row = csv_queue.get()

            cep = row[5]
            address = Utils.get_address_by_cep(cep)

            cnpj = row[0]
            partner = Partner.get_partner_by_cnpj(cnpj)
            partner_objc = PartnerService.get_partner_obj(row, address)
            if partner:
                logger.info(f'Parceiro Atualizar: ')
                logger.info(f'Parceiro obj: {partner_objc}')
                resp.append(PartnerService.upload_partner(partner_objc))
            else:
                logger.info(f'Parceiro Salvar: ')
                logger.info(f'Parceiro obj: {partner_objc}')
                resp.append(PartnerService.create_partner(partner_objc))

            csv_queue.task_done()
            done_rows += 1
            logger.info(f'Parceiro Atualizados/Salvos {done_rows}/{rows_csv}: ')
        
        return resp
            
    @staticmethod
    def get_partner_obj(data, address):
        cnpj = data[0]
        razao_social = data[1]
        nome_fantasia = data[2]
        telefone = data[3]
        email = data[4]
        cep = data[5]
        cidade = ''
        estado = ''
        if address:
            cidade = address["localidade"]
            estado = address["uf"]

        return {
            'cnpj': cnpj,
            'razao_social': razao_social,
            'nome_fantasia': nome_fantasia,
            'telefone': telefone,
            'email': email,
            'cep': cep,
            'cidade': cidade,
            'estado': estado
        }
    
    @staticmethod
    def upload_partner(partner_objc):
        return Partner.update_partner(partner_objc)
        
    @staticmethod
    def create_partner(partner_objc):
        partner_construct = Partner(partner_objc)
        partner = Partner.create_partner(partner_construct)
        if partner:
            _email_ = partner[3][1]
            EmailService.send_email(_email_)
        return partner
        