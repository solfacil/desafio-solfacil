from fastapi import status


def test_pesquisa_de_parceiros_para_apenas_um_parceiro(
    client, parceiros_teste
):
    response = client.get("/buscar?criterio=69971725000123")
    parceiros = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert parceiros[0]["cnpj"] == "69971725000123"


def test_pesquisa_de_parceiros_para_mais_de_um_parceiro(
    client, parceiros_teste
):
    response = client.get("/buscar?criterio=01156325")
    parceiros = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(parceiros) == 3


def test_pesquisa_de_parceiros_para_nenhum_parceiro(client, parceiros_teste):
    response = client.get("/buscar?criterio=84529322000112")

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_pesquisa_de_parceiros_sem_parametro_correto(client, parceiros_teste):
    response = client.get("/buscar?criterio=12")

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_consulta_parceiro_por_cnpj(client, parceiros_teste):
    response = client.get("/buscar/69971725000123")
    parceiro = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert parceiro["cnpj"] == "69971725000123"
    assert parceiro["cep"] == "01156325"


def test_consulta_cnpj_inexistente_retorna_404(client, parceiros_teste):
    response = client.get("/buscar/84529322000112")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": {"message": "Este parceiro não existe na tabela"}
    }
