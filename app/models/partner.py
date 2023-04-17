from app import db, Logger
from flask import jsonify


logger = Logger(__file__)

RETURN_FIELD_LIST = ['cnpj', 'razao_social', 'nome_fantasia', 'email', 'cidade', 'estado']
SQL_INSTANCE = '_sa_instance_state'

class Partner(db.Model):
    __tablename__ = 'partner'

    id = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.String(50), unique=True, nullable=False)
    razao_social = db.Column(db.String(50), nullable=False)
    nome_fantasia = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    cep = db.Column(db.String(50), nullable=False)
    cidade = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(50), nullable=False)

    def __init__(self, data):        
        self.cnpj = data['cnpj']
        self.razao_social = data['razao_social']
        self.nome_fantasia = data['nome_fantasia']
        self.telefone = data['telefone']
        self.email = data['email']
        self.cep = data['cep']
        self.cidade = data['cidade']
        self.estado = data['estado']

    @staticmethod
    def create_partner(partner):
        logger.info("Criando Parceiro")
        logger.info(f'partner: {partner}')
        data = []
        try:
            db.session.add(partner)
            data = [item for i, item in enumerate(partner.__dict__.items()) if i != SQL_INSTANCE and item[0] in RETURN_FIELD_LIST]
            logger.info(f'data: {data}')
        except Exception as e:
            logger.info(f'e: {str(e)}')
            db.session.rollback()
        finally:
            db.session.commit()
            return data

    @staticmethod
    def update_partner(partner_obj):
        logger.info("Atualizando Parceiro")
        logger.info(f'partner: {partner_obj}')
        data = []
        try:
            cnpj = partner_obj["cnpj"]
            partner = Partner.get_partner_by_cnpj(cnpj)
            if partner:
                partner.razao_social = partner_obj['razao_social']
                partner.nome_fantasia = partner_obj['nome_fantasia']
                partner.telefone = partner_obj['telefone']
                partner.email = partner_obj['email']
                partner.cep = partner_obj['cep']
                partner.cidade = partner_obj['cidade']
                partner.estado = partner_obj['estado']
                data = [item for i, item in enumerate(partner.__dict__.items()) if i != SQL_INSTANCE and item[0] in RETURN_FIELD_LIST]
                logger.info(f'data: {data}')
        except Exception as e:
            logger.info(f'e: {str(e)}')
            db.session.rollback()
        finally:
            db.session.commit()
            return data

    @staticmethod
    def delete_partner(cnpj):
        logger.info("Deletando Parceiro")
        logger.info(f'cnpj: {cnpj}')
        data = []
        try:
            partner = Partner.get_partner_by_cnpj(cnpj)
            if partner:
                data = [item for i, item in enumerate(partner.__dict__.items()) if item[0] != SQL_INSTANCE and item[0] in RETURN_FIELD_LIST]
                logger.info(f'data: {data}')
                db.session.delete(partner)
        except Exception as e:
            logger.info(f'e: {str(e)}')
            db.session.rollback()
        finally:
            db.session.commit()
            return data

    @staticmethod
    def get_partner_by_cnpj(cnpj):
        return Partner.query.filter_by(cnpj=cnpj).first()

    @staticmethod
    def get_all():
        data = []
        try:
            queryData = Partner.query.all()
            for query in queryData:
                for item in query.__dict__.items():
                    if item[0] != SQL_INSTANCE and item[0] in RETURN_FIELD_LIST:
                        data.append(item)
        except Exception as e:
            logger.info(f'e: {str(e)}')
        finally:
            return data
