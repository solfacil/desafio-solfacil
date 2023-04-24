from fastapi import status

from src.utils.messages import Message

message = Message()


def test_search_partners_single_partner(client, test_partners):
    response = client.get("/search?search_criteria=69971725000123")
    partners = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert partners[0]["cnpj"] == "69971725000123"


def test_search_partners_multiple_partners(client, test_partners):
    response = client.get("/search?search_criteria=01156325")
    partners = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(partners) == 3


def test_search_partners_no_partner(client, test_partners):
    response = client.get("/search?search_criteria=84529322000112")

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_search_partners_incorrect_parameter(client, test_partners):
    response = client.get("/search?search_criteria=12")

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_get_partner_by_cnpj(client, test_partners):
    response = client.get("/search/69971725000123")
    partner = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert partner["cnpj"] == "69971725000123"
    assert partner["cep"] == "01156325"


def test_get_partner_nonexistent_cnpj_returns_404(client, test_partners):
    response = client.get("/search/84529322000112")
    msg = message.get("not_found_partner")
    assert response.status_code == msg["status_code"]
    assert response.json() == {"detail": msg["detail"]}
