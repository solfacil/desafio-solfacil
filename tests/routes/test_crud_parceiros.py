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
