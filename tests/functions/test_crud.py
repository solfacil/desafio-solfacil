from src.database.crud import (
    consultar_parceiro_cnpj,
    consultar_parceiros,
    criar_parceiro,
)
from src.database.schemas import SchemaJsonParceiro


def test_novo_usuario_gera_uuid(client, db):
    cnpj_test = "kdsaldjlsa"
    cep_test = "sadasadsadsdsa"
    parceiro = SchemaJsonParceiro(**{"cnpj": cnpj_test, "cep": cep_test})

    novo_parceiro = criar_parceiro(db, parceiro)

    assert novo_parceiro.id_parceiro != ""
    assert novo_parceiro.cnpj == cnpj_test


def test_consultar_parceiros_cadastrados_retorna_parceiros_teste(
    client, db, parceiros_teste
):
    parceiros = consultar_parceiros(db)

    assert len(parceiros) == 3


def test_consultar_limitar_e_paginar_resposta(client, db, parceiros_teste):
    parceiros = consultar_parceiros(db, 1, 2)

    assert len(parceiros) == 2


def test_deve_ser_possivel_consultar_um_parceiro_pelo_cnpj(
    client, db, parceiros_teste
):
    parceiro = consultar_parceiro_cnpj(db, "1234")

    assert parceiro
    assert parceiro.cnpj == "1234"
