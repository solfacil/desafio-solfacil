from fastapi import status
from fastapi.testclient import TestClient

from src.main import app
from src.utils.messages import Message

message = Message()


def test_get_partners_should_return_200(client):
    response = client.get("/partners")
    assert response.status_code == status.HTTP_200_OK, response.text


def test_get_partners_should_return_empty_array_when_there_is_no_data(
    client,
):
    response = client.get("/partners")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []


def test_get_partners_should_return_array_when_there_is_data(
    client, test_partners
):
    response = client.get("/partners")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) != 0
    assert len(response.json()) == 3


def test_should_return_filtered_list_when_query_params_are_passed(
    client, test_partners
):
    response = client.get("/partners?skip=2&limit=1")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) != 0
    assert len(response.json()) == 1


def test_should_return_internal_server_error_when_trying_to_connect_to_db():
    client = TestClient(app)

    response = client.get("/partners")
    msg = message.get("internal_server_error")
    assert response.status_code == msg["status_code"]
    assert response.json() == {"detail": msg["detail"]}


def test_should_return_error_when_creating_partner_without_sending_json():
    client = TestClient(app)
    response = client.post("/partners")
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


def test_post_partners_should_send_payload_and_save_data_to_database(
    client, mock_zipcode_response
):
    cnpj_test = "69971725000123"
    zip_code_test = "01156325"
    response = client.post(
        "/partners", json={"cnpj": cnpj_test, "cep": zip_code_test}
    )
    created_partner = response.json()
    assert response.status_code == status.HTTP_201_CREATED
    assert created_partner["id_parceiro"] != ""
    assert created_partner["cnpj"] == cnpj_test
    assert created_partner["cep"] == zip_code_test


def test_post_partners_should_return_error_when_create_an_existing_user(
    client, test_partners
):
    cnpj_test = "69971725000123"
    cep_test = "01156325"
    response = client.post(
        "/partners", json={"cnpj": cnpj_test, "cep": cep_test}
    )
    msg = message.get("unique_constraint_error")
    assert response.status_code == msg["status_code"]
    assert response.json() == {"detail": msg["detail"]}


def test_post_partners_should_return_error_when_create_with_invalid_cnpj(
    client, test_partners
):
    cnpj_test = "ndskadnslajd"
    cep_test = "01156325"
    response = client.post(
        "/partners", json={"cnpj": cnpj_test, "cep": cep_test}
    )

    msg = message.get("cnpj_invalid")
    assert response.status_code == msg["status_code"]
    assert response.json() == {"detail": msg["detail"]}


def test_post_partners_should_return_error_when_create_with_invalid_zip_code(
    client, mock_zipcode_response_error
):
    test_cnpj = "69971725000123"
    test_zip_code = "01156325"
    response = client.post(
        "/partners", json={"cnpj": test_cnpj, "cep": test_zip_code}
    )
    msg = message.get("zip_code_invalid")
    assert response.json() == {"detail": msg["detail"]}
    assert response.status_code == msg["status_code"]


def test_update_partner_information(client, test_partners):
    test_cnpj = "69971725000123"

    response = client.get(f"/search/{test_cnpj}")
    partner = response.json()

    response = client.put(
        f"/partners/{test_cnpj}",
        json={"cnpj": test_cnpj, "email": "company@123.com"},
    )
    updated_partner = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert updated_partner["id_parceiro"] == partner["id_parceiro"]
    assert updated_partner["cnpj"] == partner["cnpj"]
    assert updated_partner["email"] != partner["email"]


def test_update_partner_returns_404_if_not_found(client, test_partners):
    test_cnpj = "84529322000112"
    test_zip_code = "01156325"
    response = client.put(
        f"/partners/{test_cnpj}",
        json={"cnpj": test_cnpj, "cep": test_zip_code},
    )
    msg = message.get("not_found_partner")
    assert response.status_code == msg["status_code"]
    assert response.json() == {"detail": msg["detail"]}


def test_update_partner_with_wrong_zip_code(
    client, test_partners, requests_mock
):
    url = "https://viacep.com.br/ws/69314690/json/"
    json = {"erro": True}

    requests_mock.get(url, status_code=200, json=json)

    test_cnpj = "16470954000106"
    test_zip_code = "69314690"
    response = client.put(
        f"/partners/{test_cnpj}",
        json={"cnpj": test_cnpj, "cep": test_zip_code},
    )
    msg = message.get("zip_code_invalid")
    assert response.status_code == msg["status_code"]
    assert response.json() == {"detail": msg["detail"]}


def test_delete_partner(client, test_partners):
    response = client.delete("/partners/69971725000123")
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_delete_nonexistent_partner(client, test_partners):
    response = client.delete("/partners/84529322000112")
    assert response.status_code == status.HTTP_404_NOT_FOUND
