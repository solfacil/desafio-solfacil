from flask import Blueprint, jsonify
from app.services.partner import PartnerService
from app import Logger

logger = Logger(__file__)

partner_blueprint = Blueprint('partner', __name__)

@partner_blueprint.route('/list_all_partners', methods=['GET'])
def list_all_partners():
    try:
        logger.info("GET - Listar Parceiros")
        partners = PartnerService.list_all_partners()
        if partners:
            logger.info("Lista de Parceiros")
            logger.info(f"Parceiros {partners}")
            return jsonify({
                    'message': 'Todos os Parceiros cadatsrados no banco!',
                    'partners': partners
                }), 200
        return jsonify({
            'message': 'Nenhum Parceiro cadatrado no banco!',
            'partners': partners
            }), 200
    except Exception as e:
        logger.info(f'e: {str(e)}')
        return jsonify({
            'error': 'Erro! Ao listar Parceiros.', 
            'details': str(e)
            }), 500
    