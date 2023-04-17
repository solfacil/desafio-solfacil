from flask import Blueprint, request, jsonify
from app.services.csv import CSVService
from app.services.partner import PartnerService
from app import Logger

logger = Logger(__file__)

csv_blueprint = Blueprint('csv', __name__)

@csv_blueprint.route('/upload_partner', methods=['POST'])
def upload_partner():
    try:
        logger.info("POST - Upload Parceiro CSV")
        file = request.files['file']
        data = CSVService.read_partner_csv(file)
        if not data:
            logger.info("CSV Vazio")
            logger.info(f"csv {data}")
            return jsonify({
                'message': 'Nenhum dado de Upload dos Parceiros foi encontrado!',
                'data': data
            }), 200
        
        valid_data = CSVService.validate_partner_upload_csv(data)
        if not valid_data:
            logger.info("CSV com campos inválidos")
            logger.info(f"csv {data}")
            return jsonify({
                'message': 'Nenhum dos dados de Upload dos Parceiros são válidos!',
                'data': valid_data
            }), 200
        
        resp = PartnerService.upload_csv_partner(valid_data)
        if resp:
            logger.info("Parceiros Salvos/Atualizados")
            logger.info(f"Parceiros {resp}")
            return jsonify({
                'message': f'De {len(valid_data)} Parceiros, {len(resp)} foram atualizados ou salvos!',
                'data': resp
            }), 200

        logger.info("Nenhum Parceiro Salvos/Atualizado")
        return jsonify({
            'message': 'Erro! Nenhum dos Parceiros foi salvo ou atualizado!',
            'data': []
            }), 500
    except Exception as e:
        logger.info(f'e: {str(e)}')
        return jsonify({
            'error': 'Erro! Ao Carregar CSV dos Parceiros.', 
            'details': str(e)
            }), 500
    
