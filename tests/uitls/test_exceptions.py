from unittest.mock import Mock

import pytest
from fastapi import HTTPException, status

from src.utils import response_exception


def test_se_receber_um_erro_sem_tratativa_deve_retornar_um_500():
    mock_exception = Mock()
    mock_exception.side_effect = Exception
    mock_exception.return_value = None
    with pytest.raises(HTTPException) as exc_info:
        response_exception(mock_exception)
    assert exc_info.value.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    assert exc_info.value.detail == {"message": "Internal server error"}


def test_se_receber_de_violacao_de_constraint_deve_retornar_422():
    with pytest.raises(HTTPException) as exc_info:
        response_exception("Violation unique constraint, valor ja existe")
    assert exc_info.value.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert exc_info.value.detail == {
        "message": "Este parceiro ja existe na tabela"
    }


def test_se_receber_um_httpexception_deve_retornalo_como_erro():
    error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail={"message": "Usuario não autorizado"},
    )
    with pytest.raises(HTTPException) as exc_info:
        response_exception(error)
    assert exc_info.value.status_code == status.HTTP_401_UNAUTHORIZED
    assert exc_info.value.detail == {"message": "Usuario não autorizado"}
