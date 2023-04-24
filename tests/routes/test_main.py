from platform import python_version


def test_get_root_should_return_200_and_python_version(client):
    response = client.get("/")
    assert response.status_code == 200, response.text
    assert response.json() == {"python_version": python_version()}
