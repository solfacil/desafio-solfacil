from src.database.crud import consultar_parceiros, criar_parceiro
from src.database.schemas import SchemaCriacaoParceiro


def test_ao_criar_um_parceiro_deve_retornar_o_uuid(client, db):
    cnpj_test = "kdsaldjlsa"
    cep_test = "sadasadsadsdsa"
    parceiro = SchemaCriacaoParceiro(**{"cnpj": cnpj_test, "cep": cep_test})

    novo_parceiro = criar_parceiro(db, parceiro)

    assert novo_parceiro.id_parceiro != ""
    assert novo_parceiro.cnpj == cnpj_test


def test_ao_consultar_os_parceiros_cadastrados_deve_retornar_testers(
    client, db, parceiros_teste
):
    parceiros = consultar_parceiros(db)

    assert len(parceiros) == 3
