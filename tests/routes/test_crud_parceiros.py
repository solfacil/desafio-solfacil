def test_create_user(client):
    response = client.get("/parceiros")
    assert response.status_code == 200, response.text
