from fastapi import status


def test_endpoint_com_csv(client):
    response = client.post(
        "/upload/parceiros",
        files={
            "file": (
                "assets/exemplo.csv",
                open("assets/exemplo.csv", "rb"),
                "text/csv",
            )
        },
    )
    assert response.status_code == status.HTTP_200_OK


def test_endpoint_com_csv_errado(client):
    response = client.post(
        "/upload/parceiros",
        files={
            "file": (
                "assets/exemplo.csv",
                open("assets/exemplo errado.csv", "rb"),
                "text/csv",
            )
        },
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": {
            "message": "O formato deste arquivo CSV não está correto. \
Por favor, verifique as colunas e tente novamente."
        }
    }


def test_endpoint_com_csv_para_atualizacao(
    client, parceiros_teste, requests_mock
):
    url = "https://viacep.com.br/ws/69314690/json/"
    json = {"erro": True}

    requests_mock.get(url, status_code=200, json=json)
    response = client.post(
        "/upload/parceiros",
        files={
            "file": (
                "assets/tests.csv",
                open("assets/tests.csv", "rb"),
                "text/csv",
            )
        },
    )
    assert response.status_code == status.HTTP_200_OK


def test_endpoint_com_csv_e_cep_errado(client, parceiros_teste, requests_mock):
    url = "https://viacep.com.br/ws/69314690/json/"
    json = {"erro": True}

    requests_mock.get(url, status_code=200, json=json)

    response = client.post(
        "/upload/parceiros",
        files={
            "file": (
                "assets/tests.csv",
                open("assets/tests.csv", "rb"),
                "text/csv",
            )
        },
    )
    assert response.status_code == status.HTTP_200_OK
