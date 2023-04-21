import requests
from sqlalchemy.orm import Session

from src.database.models import CepInfo


def salva_novo_cep(db: Session, cep: str):
    cep_infos = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))

    if "erro" not in cep_infos.json():
        novo_cep = cep_infos.json()
        novo_cep["cep"] = cep
        cep_json = CepInfo(**novo_cep)
        db.add(cep_json)
        db.commit()
        db.refresh(cep_json)
        return True
    else:
        return False


def verifica_cep(db: Session, cep: str):
    cep = "".join(filter(str.isdigit, cep))
    cep_info_db = db.query(CepInfo).filter(CepInfo.cep == cep).first()

    if not cep_info_db:
        return salva_novo_cep(db, cep)

    return True
