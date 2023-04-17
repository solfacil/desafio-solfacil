from app import Logger

logger = Logger(__file__)

class EmailService:
    @staticmethod
    def send_email(email):
        logger.info(f"Enviando E-mail para {email}")