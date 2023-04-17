from app.models.partner import Partner
import csv
import io
from app.services.partner import PartnerService
from app import Logger

logger = Logger(__file__)

class CSVService:
    @staticmethod
    def read_partner_csv(file):
        logger.info('Lendo CSV...')
        content = file.stream.read().decode('utf-8')
        file_reader = csv.reader(io.StringIO(content), delimiter=',')
        data = []
        for row in file_reader:
            data.append(row)
        logger.info(f'data: {data}')
        return data
    
    @staticmethod
    def validate_partner_upload_csv(data):
        logger.info('Verificando campos...')
        valid_data = []
        for row in data[1:]: # data[0] = header 
            if PartnerService.valid_partner_values(row):
                valid_data.append(row)
        logger.info(f'valid_data: {valid_data}')
        return valid_data
        