from dotenv import load_dotenv

load_dotenv()

import json
import logging
import os

import log
from database import DB
from definitions import BASE_DIR, __version__, db_infos
from fastapi import APIRouter, FastAPI, status
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from fastapi_pagination import add_pagination
from loguru import logger
from routes import home, partner
from schemas import *  # noqa: F403, F401
from schemas.Base import Base
from starlette.requests import Request
from uvicorn import Config, Server

# --------------------------------------------------

app = FastAPI(title="EasySun")

api_router = APIRouter(prefix="/api")
api_router.include_router(partner.router)

app.include_router(api_router)
app.include_router(home.router)

add_pagination(app)

DB.connect(**db_infos)
Base.metadata.create_all(DB.engine)

# --------------------------------------------------


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):

    dump_path = BASE_DIR / "logs" / 'error_request.json'
    if not dump_path.parent.exists():
        dump_path.parent.mkdir(parent=True)

    try:
        with dump_path.open('w') as f:
            if isinstance(exc.body, (list, dict)):
                json.dump(exc.body, f, indent=4, default=str)
            else:
                f.write(str(exc.body))
        logger.critical(f"Request com erro foi salvo em: '{str(dump_path)}'")
    except Exception as e:
        logger.critical(f"Erro ao salvar o body: '{e}'")

    exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
    logger.error(f"{exc_str}")
    content = {'status_code': 10422, 'message': exc_str, 'data': None}
    return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


# --------------------------------------------------

if __name__ == '__main__':

    logger.critical(f"API Version = '{__version__}'")

    trusted_hosts = os.environ.get('APP_TRUSTED_HOSTS', '*')
    trusted_hosts = trusted_hosts.split(',')
    if not isinstance(trusted_hosts, list):
        trusted_hosts = [trusted_hosts]

    logger.critical(f"Trusted hosts: {trusted_hosts}")
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=trusted_hosts)

    log_level = logging.getLevelName(os.environ.get('LOG_LEVEL', "DEBUG"))

    server = Server(
        Config(
            app,
            host=os.environ.get('APP_IP', '0.0.0.0'),
            port=int(os.environ.get('APP_PORT', 8080)),
            log_level=log_level,
        ),
    )  # yapf: disable

    # setup logging last, to make sure no library overwrites it
    # (they shouldn't, but it happens)
    log_options = {
        'level': os.environ.get('LOG_LEVEL', 'DEBUG'),
        'rotation': os.environ.get('LOG_ROTATION', "00:00"),
        'compression': os.environ.get('LOG_COMPRESSION', "zip"),
        'retention': os.environ.get('LOG_RETENTION', "30 days")
    }
    log.setup_logging(BASE_DIR, **log_options)

    server.run()
