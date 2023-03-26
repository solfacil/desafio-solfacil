from definitions import __version__ as app_version
from fastapi import APIRouter, status
from loguru import logger  # noqa: F401

# --------------------------------------------------

router = APIRouter(prefix='', tags=["index"])

# --------------------------------------------------


@router.get("/", status_code=status.HTTP_200_OK)
async def index():
    return {'status': "running", "version": app_version}
