import logging

from fastapi import HTTPException

from src.utils.messages import Message

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

messages = Message()


def response_exception(e):
    if "unique constraint" in str(e).lower():
        message = messages.get("unique_constraint_error")
    elif "Not Found Partner" in str(e):
        message = messages.get("not_found_partner")
    elif "Invalid Zip Code" in str(e):
        message = messages.get("zip_code_invalid")
    elif "Invalid CNPJ" in str(e):
        message = messages.get("cnpj_invalid")
    elif "CSV is not valid columns" in str(e):
        message = messages.get("csv_is_not_valid_columns")
    elif "CSV is not valid rows" in str(e):
        message = messages.get("csv_is_not_valid_rows")
    elif not isinstance(e, HTTPException):
        message = messages.get("internal_server_error")
    else:
        raise e
    raise HTTPException(**message)
