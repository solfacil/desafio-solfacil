from fastapi import status
from fastapi.testclient import TestClient

from src.main import app


def test_get_parceiros_devera_retornar_200(client):
    response = client.get("/parceiros")
    assert response.status_code == status.HTTP_200_OK, response.text


def test_get_parceiros_deve_retornar_um_array_vazio_quando_nao_houver_dados(
    client,
):
    response = client.get("/parceiros")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []


def test_get_parceiros_deve_retornar_um_array_quando_houver_dados(
    client, parceiros_teste
):
    response = client.get("/parceiros")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) != 0
    assert len(response.json()) == 3


def test_deve_retornar_lista_filtrada_quando_passar_query_params(
    client, parceiros_teste
):
    response = client.get("/parceiros?skip=2&limit=1")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) != 0
    assert len(response.json()) == 1


def test_consulta_parceiro_por_cnpj(client, parceiros_teste):
    response = client.get("/parceiros/1234")
    parceiro = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert parceiro["cnpj"] == "1234"
    assert parceiro["cep"] == "sadsa"


def test_consulta_cnpj_inexistente_retorna_404(client, parceiros_teste):
    response = client.get("/parceiros/12345")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": {"message": "Este parceiro não existe na tabela"}
    }


def test_ao_tentar_conectar_com_banco_deve_retornar_erro_interno_sem_conexao():
    client = TestClient(app)

    response = client.get("/parceiros")
    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    assert response.json() == {"detail": {"message": "Internal server error"}}


def test_ao_criar_parceiro_sem_enviar_json_deve_retornar_erro():
    client = TestClient(app)
    response = client.post("/parceiros")
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": [
            {
                "loc": ["body"],
                "msg": "field required",
                "type": "value_error.missing",
            }
        ]
    }


def test_post_parceiros_deve_enviar_o_payload_do_e_salvar_os_dados_no_banco(
    client,
):
    cnpj_test = "kdsaldjlsa"
    cep_test = "sadasadsadsdsa"
    response = client.post(
        "/parceiros", json={"cnpj": cnpj_test, "cep": cep_test}
    )
    parceiro_criado = response.json()
    assert response.status_code == status.HTTP_201_CREATED
    assert parceiro_criado["id_parceiro"] != ""
    assert parceiro_criado["cnpj"] == cnpj_test
    assert parceiro_criado["cep"] == cep_test


def test_post_parceiros_deve_dar_erro_ao_tentar_criar_um_usuario_que_ja_existe(
    client, parceiros_teste
):
    cnpj_test = "1234"
    cep_test = "sadasadsadsdsa"
    response = client.post(
        "/parceiros", json={"cnpj": cnpj_test, "cep": cep_test}
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": {"message": "Este parceiro ja existe na tabela"}
    }


def test_atualizar_informacoes_parceiro(client, parceiros_teste):
    cnpj_test = "1234"
    cep_test = "sadasadsadsdsa"

    response = client.get("/parceiros/1234")
    parceiro = response.json()

    response = client.put(
        "/parceiros/1234", json={"cnpj": cnpj_test, "cep": cep_test}
    )
    parceiro_atualizado = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert parceiro_atualizado["id_parceiro"] == parceiro["id_parceiro"]
    assert parceiro_atualizado["cnpj"] == parceiro["cnpj"]
    assert parceiro_atualizado["cep"] != parceiro["cep"]


def test_atualizacao_de_parceiro_retorna_404_se_nao_existir(
    client, parceiros_teste
):
    cnpj_test = "1234"
    cep_test = "sadasadsadsdsa"
    response = client.put(
        "/parceiros/12345", json={"cnpj": cnpj_test, "cep": cep_test}
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": {"message": "Este parceiro não existe na tabela"}
    }


def test_exclusao_de_parceiro(client, parceiros_teste):
    response = client.delete("/parceiros/1234")
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_exclusao_de_parceiro_inexistente(client, parceiros_teste):
    response = client.delete("/parceiros/12345")
    assert response.status_code == status.HTTP_404_NOT_FOUND
