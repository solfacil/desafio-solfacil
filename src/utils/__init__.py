import logging

from fastapi import HTTPException, status

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def response_exception(e):
    if isinstance(e, HTTPException):
        logger.error(
            "status_code: {}, message: {}".format(e.status_code, e.detail)
        )
        raise e
    elif "unique constraint" in str(e).lower():
        handle_unique_constraint_error(e)
    else:
        logger.error(
            "status_code: {}, message: {}".format(
                status.HTTP_500_INTERNAL_SERVER_ERROR, str(e)
            )
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"message": "Internal server error"},
        )


def handle_unique_constraint_error(e):
    logger.error(
        "status_code: {}, message: {}".format(
            status.HTTP_422_UNPROCESSABLE_ENTITY, str(e)
        )
    )
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail={"message": "Este parceiro ja existe na tabela"},
    )
