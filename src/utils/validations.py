from sqlalchemy.orm import Session
from validate_docbr import CNPJ

from src.database.schemas import PartnerJsonSchema
from src.utils.messages import Message
from src.utils.string_to_snake import snake_case
from src.utils.zip_code_search import verify_zip_code

columns = ["cnpj", "razao_social", "nome_fantasia", "telefone", "email", "cep"]

messages = Message("validation")


def validate_cnpj_zip_code(db: Session, partner):
    if not CNPJ().validate(partner["cnpj"]):
        return messages.get("partner_cnpj_is_not_valid")

    if not verify_zip_code(db, partner["cep"]):
        return messages.get("partner_zip_code_is_not_found")

    return messages.get("partner_is_valid")


def validate_csv(db: Session, headers, rows):
    headers = [snake_case(h) for h in headers]
    has_columns = all(column in columns for column in headers)

    if not has_columns:
        raise Exception("CSV is not valid columns")

    status_partners = {}
    valid_partners = []

    for row in rows:
        partner = {}

        if len(row) != len(columns):
            raise Exception("CSV is not valid rows")

        for index in range(len(row)):
            if headers[index] == "cnpj":
                partner[headers[index]] = "".join(
                    filter(str.isdigit, row[index])
                )
            else:
                partner[headers[index]] = row[index]

        cnpj_partner = partner["cnpj"]
        status_partners[cnpj_partner] = validate_cnpj_zip_code(db, partner)

        if status_partners[cnpj_partner]["status"]:
            valid_partners.append(PartnerJsonSchema.parse_obj(partner))

    return {"partners": valid_partners, "status": status_partners}
