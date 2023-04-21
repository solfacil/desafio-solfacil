from src.database.crud import create_partner, list_partners
from src.database.schemas import SchemaJsonParceiro
from src.database.search import consult_partner_cnpj


def test_novo_usuario_gera_uuid(client, db, mock_cep_response):
    cnpj_test = "84529322000112"
    cep_test = "01156325"
    parceiro = SchemaJsonParceiro(**{"cnpj": cnpj_test, "cep": cep_test})

    novo_parceiro = create_partner(db, parceiro)

    assert novo_parceiro.id_parceiro != ""
    assert novo_parceiro.cnpj == cnpj_test


def test_consultar_parceiros_cadastrados_retorna_parceiros_teste(
    client, db, parceiros_teste
):
    parceiros = list_partners(db)

    assert len(parceiros) == 3


def test_consultar_limitar_e_paginar_resposta(client, db, parceiros_teste):
    parceiros = list_partners(db, 1, 2)

    assert len(parceiros) == 2


def test_deve_ser_possivel_consultar_um_parceiro_pelo_cnpj(
    client, db, parceiros_teste
):
    parceiro = consult_partner_cnpj(db, "69971725000123")

    assert parceiro
    assert parceiro.cnpj == "69971725000123"
