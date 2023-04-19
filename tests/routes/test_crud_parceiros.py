def test_get_parceiros_devera_retornar_200(client):
    response = client.get("/parceiros")
    assert response.status_code == 200, response.text
