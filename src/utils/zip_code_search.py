import requests
from sqlalchemy.orm import Session

from src.database.models import ZipCodeInfo
from src.database.schemas import ZipCodeJsonSchema


def verify_zip_code(db: Session, zip_code: str):
    zip_code = "".join(filter(str.isdigit, zip_code))
    has_zip_code = (
        db.query(ZipCodeInfo).filter(ZipCodeInfo.zip_code == zip_code).first()
    )

    if not has_zip_code:
        zip_code_information = requests.get(
            "https://viacep.com.br/ws/{}/json/".format(zip_code)
        )

        if "erro" not in zip_code_information.json():
            new_zip_code = ZipCodeJsonSchema(**zip_code_information.json())
            zip_code_json = ZipCodeInfo(**new_zip_code.dict())
            db.add(zip_code_json)
            db.commit()
            db.refresh(zip_code_json)
        else:
            return False

    return True
