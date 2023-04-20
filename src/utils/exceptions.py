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
    elif "not found" in str(e).lower():
        handle_not_found_error(e)
    elif "csv is not formated" in str(e).lower():
        handle_csv_not_formated(e)
    elif "cep invalid" in str(e).lower():
        handle_cep_invalid(e)
    elif "cnpj invalid" in str(e).lower():
        handle_cnpj_invalid(e)
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


def handle_not_found_error(e):
    logger.error(
        "status_code: {}, message: {}".format(
            status.HTTP_404_NOT_FOUND, str(e)
        )
    )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={"message": "Este parceiro não existe na tabela"},
    )


def handle_csv_not_formated(e):
    logger.error(
        "status_code: {}, message: {}".format(
            status.HTTP_422_UNPROCESSABLE_ENTITY, str(e)
        )
    )
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail={
            "message": "O formato deste arquivo CSV não está correto. \
Por favor, verifique as colunas e tente novamente."
        },
    )


def handle_cnpj_invalid(e):
    logger.error(
        "status_code: {}, message: {}".format(
            status.HTTP_422_UNPROCESSABLE_ENTITY, str(e)
        )
    )
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail={
            "message": "A empresa informada possui um CNPJ inválido. \
Por favor, verifique o número digitado e tente novamente."
        },
    )


def handle_cep_invalid(e):
    logger.error(
        "status_code: {}, message: {}".format(
            status.HTTP_422_UNPROCESSABLE_ENTITY, str(e)
        )
    )
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail={
            "message": "A empresa informada possui um CEP inválido. \
Por favor, verifique o número digitado e tente novamente."
        },
    )
