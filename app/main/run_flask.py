from flask import Flask
from app.interfaces.api.flask.main_router import main_router

app = Flask(__name__)

app.register_blueprint(main_router, url_prefix='/api')
