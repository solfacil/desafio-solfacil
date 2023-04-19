def test_get_parceiros_devera_retornar_200(client):
    response = client.get("/parceiros")
    assert response.status_code == 200, response.text


def test_get_parceiros_deve_retornar_um_array_vazio_quando_nao_houver_dados(
    client,
):
    response = client.get("/parceiros")
    assert response.json() == []
