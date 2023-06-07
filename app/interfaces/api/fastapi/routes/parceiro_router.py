import logging
from typing import Dict, List, Annotated

from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from pydantic import ValidationError

from app.application.dtos.parceiro_dto import ParceiroDto
from app.interfaces.api.controller.parceiro_controller import get_controller, ParceiroController

router = APIRouter()

async def common_params(
        controller: Annotated[ParceiroController, Depends(get_controller)]):
    return controller

@router.post(
    "/parceiros/upload_csv",
    response_model=Dict[str, List[ParceiroDto]],
    status_code=200,
)
async def upload_csv(
        controller: Annotated[ParceiroController, Depends(common_params)],
        file: UploadFile = File(...),
):
    content = await file.read()
    try:
        parceiros = await controller.upload_csv(content.decode())
    except ValidationError as err:
        raise HTTPException(status_code=400, detail=err.errors()) from err
    except Exception as err:
        logging.critical(err)
        raise HTTPException(status_code=500, detail=str(err)) from err
    return parceiros


@router.get(
    "/parceiros",
    response_model=list[ParceiroDto],
    status_code=200,
)
async def get_all_parceiros(
        controller: Annotated[ParceiroController, Depends(common_params)],
):
    try:
        return await controller.get_all_parceiros()
    except Exception as err:
        logging.critical(err)
        raise HTTPException(status_code=500, detail=str(err))
