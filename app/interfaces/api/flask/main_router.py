from flask import Blueprint
from app.interfaces.api.flask.routes.parceiro_router import parceiro_bp

main_router = Blueprint('main_router', __name__)

main_router.register_blueprint(parceiro_bp)

