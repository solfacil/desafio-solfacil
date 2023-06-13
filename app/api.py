from app import cep, database, email, utils
import csv
import codecs

def upload_csv(file):
    csv_reader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
    data_to_upsert = []
    cep_to_upsert = []

    for row in csv_reader:
        if utils.validate_cnpj(row['CNPJ']) and utils.validate_email(row['Email']):
            data = row
            data["CNPJ"] = utils.parse_cnpj(data['CNPJ'])
            data["address"] = cep.request_cep(row["CEP"])
            data["Telefone"] = utils.parse_phone(row["Telefone"])
            cep_to_upsert.append(data["address"])
            data_to_upsert.append(data)

    file.file.close()

    # Upsert Database
    database.upsert_cep(cep_to_upsert)
    database.upsert_partners(data_to_upsert)

    #get users to send email
    result = database.get_users_to_send_emails()
    if len(result) > 0:
        email.send_email(result)
        database.upsert_email_has_send(result)
    
    return data_to_upsert
