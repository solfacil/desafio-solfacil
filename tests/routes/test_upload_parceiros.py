from fastapi import status


def test_endpoint_com_csv(client):
    response = client.post(
        "/upload/parceiros",
        files={
            "file": (
                "massa_de_testes.csv",
                open("tests/assets/massa_de_testes.csv", "rb"),
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
                "formato_errado.csv",
                open("tests/assets/formato_errado.csv", "rb"),
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
    json = {
        "cep": "01156-325",
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
        "/upload/parceiros",
        files={
            "file": (
                "parceiro_existente.csv",
                open("tests/assets/parceiro_existente.csv", "rb"),
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
                "parceiro_existente.csv",
                open("tests/assets/parceiro_existente.csv", "rb"),
                "text/csv",
            )
        },
    )
    assert response.status_code == status.HTTP_200_OK
