import logging

from flask import request, jsonify, abort, Blueprint
from pydantic import ValidationError
from werkzeug.datastructures import FileStorage

from app.interfaces.api.controller.parceiro_controller import get_controller
from app.interfaces.api.flask.helpers.async_helper import execute_async_to_sync

parceiro_bp = Blueprint('parceiro', __name__)

@parceiro_bp.route('/parceiros/upload_csv', methods=['POST'])
def upload_csv():
    controller = execute_async_to_sync(get_controller)

    if 'file' not in request.files:
        abort(400, 'No file part')

    file = request.files['file']
    if file.filename == '':
        abort(400, 'No selected file')

    if file and isinstance(file, FileStorage):
        content = file.read().decode()
        try:
            parceiros = execute_async_to_sync(controller.upload_csv, content)
            return jsonify(parceiros), 200
        except ValidationError as err:
            abort(400, str(err))
        except Exception as err:
            logging.critical(err)
            abort(500, str(err))

@parceiro_bp.route('/parceiros', methods=['GET'])
def get_all_parceiros():
    controller = execute_async_to_sync(get_controller)
    try:
        parceiros = execute_async_to_sync(controller.get_all_parceiros)
        return jsonify([p.json() for p in parceiros]), 200
    except Exception as err:
        logging.critical(err)
        abort(500, str(err))
