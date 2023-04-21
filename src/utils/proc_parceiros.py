from sqlalchemy.orm import Session
from validate_docbr import CNPJ

from src.database.crud import create_partner, update_partner
from src.database.schemas import SchemaJsonParceiro
from src.utils.busca_cep import verifica_cep
from src.utils.string_to_snake import snake_case

colunas = ["cnpj", "razao_social", "nome_fantasia", "telefone", "email", "cep"]


def valida_cnpj_cep(db: Session, parceiro):
    cnpj_verify = CNPJ()
    if not cnpj_verify.validate(parceiro["cnpj"]):
        return {"Status": False, "Message": "CNPJ Inválido"}

    if not verifica_cep(db, parceiro["cep"]):
        return {"Status": False, "Message": "CEP Inválido"}

    return {"Status": True}


def processar(db: Session, headers: list[str], rows: list[str]):
    headers = [snake_case(h) for h in headers]
    if colunas != headers:
        raise Exception("csv is not formated")

    status_parceiros = {}
    items_parceiros = []
    for row in rows:
        parceiro = {}

        for index in range(len(row)):
            parceiro[headers[index]] = row[index]

        validacao = valida_cnpj_cep(db, parceiro)
        if validacao["Status"]:
            parceiro_validado = SchemaJsonParceiro(**parceiro)
            items_parceiros.append(parceiro_validado)
            status_parceiros[parceiro_validado.cnpj] = {
                "Message": "Validado!",
                "Detail": "",
            }
        else:
            status_parceiros[parceiro["cnpj"]] = {
                "Message": "Error!",
                "Detail": validacao["Message"],
            }

    for parceiro in items_parceiros:
        try:
            update_partner(db, parceiro.cnpj, parceiro)
            msg = "Parceiro atualizado com sucesso!"
        except Exception:
            create_partner(db, parceiro).serialize()
            msg = "Parceiro criado com sucesso!"
        finally:
            status_parceiros[parceiro.cnpj] = {"Message": msg}

    return status_parceiros
