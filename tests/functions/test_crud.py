from src.database.crud import create_partner, list_partners
from src.database.schemas import PartnerJsonSchema
from src.database.search import consult_partner_cnpj


def test_new_user_generates_uuid(client, db, mock_zipcode_response):
    cnpj_test = "84529322000112"
    zip_code_test = "01156325"
    partner = PartnerJsonSchema.parse_obj(
        {"cnpj": cnpj_test, "cep": zip_code_test}
    )

    new_partner = create_partner(db, partner)

    assert new_partner.partner_id != ""
    assert new_partner.cnpj == cnpj_test


def test_list_registered_partners_returns_test_partners(
    client, db, test_partners
):
    partners = list_partners(db)

    assert len(partners) == 3


def test_limit_and_paginate_response(client, db, test_partners):
    partners = list_partners(db, 1, 2)

    assert len(partners) == 2


def test_it_should_be_possible_to_consult_a_partner_by_cnpj(
    client, db, test_partners
):
    partner = consult_partner_cnpj(db, "69971725000123")

    assert partner
    assert partner.cnpj == "69971725000123"
