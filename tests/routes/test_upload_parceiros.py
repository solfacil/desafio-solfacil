from fastapi import status

from src.utils.messages import Message

message = Message()


def test_endpoint_with_csv(client):
    response = client.post(
        "/upload/partners",
        files={
            "file": (
                "test_data.csv",
                open("tests/assets/test_data.csv", "rb"),
                "text/csv",
            )
        },
    )
    assert response.status_code == status.HTTP_200_OK


def test_endpoint_with_wrong_csv_columns(client):
    response = client.post(
        "/upload/partners",
        files={
            "file": (
                "wrong_format_columns.csv",
                open("tests/assets/wrong_format_columns.csv", "rb"),
                "text/csv",
            )
        },
    )

    msg = message.get("csv_is_not_valid_columns")
    assert response.status_code == msg["status_code"]
    assert response.json() == {"detail": msg["detail"]}


def test_endpoint_with_wrong_csv_rows(client):
    response = client.post(
        "/upload/partners",
        files={
            "file": (
                "wrong_format_rows.csv",
                open("tests/assets/wrong_format_rows.csv", "rb"),
                "text/csv",
            )
        },
    )

    msg = message.get("csv_is_not_valid_rows")
    assert response.status_code == msg["status_code"]
    assert response.json() == {"detail": msg["detail"]}


def test_endpoint_with_csv_for_update(client, test_partners, requests_mock):
    url = "https://viacep.com.br/ws/69314690/json/"
    json = {
        "cep": "69314-690",
        "logradouro": "Rua Patativa da Santa Maria",
        "complemento": "",
        "bairro": "Colônia Dona Luíza",
        "localidade": "Ponta Grossa",
        "uf": "PR",
        "ibge": "4119905",
        "gia": "",
        "ddd": "42",
        "siafi": "7777",
    }

    requests_mock.get(url, status_code=200, json=json)
    response = client.post(
        "/upload/partners",
        files={
            "file": (
                "existing_partner.csv",
                open("tests/assets/existing_partner.csv", "rb"),
                "text/csv",
            )
        },
    )
    assert response.status_code == status.HTTP_200_OK


def test_endpoint_with_csv_and_wrong_zip_code(
    client, test_partners, requests_mock
):
    url = "https://viacep.com.br/ws/69314690/json/"
    json = {"erro": True}

    requests_mock.get(url, status_code=200, json=json)

    response = client.post(
        "/upload/partners",
        files={
            "file": (
                "existing_partner.csv",
                open("tests/assets/existing_partner.csv", "rb"),
                "text/csv",
            )
        },
    )
    assert response.status_code == status.HTTP_200_OK
