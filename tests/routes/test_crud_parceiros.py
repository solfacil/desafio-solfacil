from fastapi.testclient import TestClient

from src.main import app


def test_get_parceiros_devera_retornar_200(client):
    response = client.get("/parceiros")
    assert response.status_code == 200, response.text


def test_get_parceiros_deve_retornar_um_array_vazio_quando_nao_houver_dados(
    client,
):
    response = client.get("/parceiros")
    assert response.json() == []


def test_get_parceiros_deve_retornar_um_array_quando_houver_dados(
    client, parceiros_teste
):
    response = client.get("/parceiros")
    assert response.status_code == 200
    assert len(response.json()) != 0
    assert len(response.json()) == 3


def test_deve_retornar_lista_filtrada_quando_passar_query_params(
    client, parceiros_teste
):
    response = client.get("/parceiros?skip=2&limit=1")
    assert response.status_code == 200
    assert len(response.json()) != 0
    assert len(response.json()) == 1


def test_ao_tentar_conectar_com_banco_deve_retornar_erro_interno_sem_conexao():
    client = TestClient(app)

    response = client.get("/parceiros")
    assert response.status_code == 500
    assert response.json() == {"detail": {"message": "Internal server error"}}


def test_ao_criar_parceiro_sem_enviar_json_deve_retornar_erro():
    client = TestClient(app)
    response = client.post("/parceiros")
    assert response.status_code == 422
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
    assert response.status_code == 201
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
    assert response.status_code == 422
    assert response.json() == {
        "detail": {"message": "Este parceiro ja existe na tabela"}
    }
