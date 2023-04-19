from platform import python_version


def test_get_na_raiz_devera_retornar_200_e_a_versao_python(client):
    response = client.get("/")
    assert response.status_code == 200, response.text
    assert response.json() == {"python_version": python_version()}
