import re
import requests
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from ..crud import crud
from ..model import parteners


def valida_cnpj(cnpj):
    cnpj = re.sub(r'[^0-9]', '', cnpj) 
    if len(cnpj) != 14:
        return False
    soma = 0
    for i in range(12):
        soma += int(cnpj[i]) * ((5,4,3,2,9,8,7,6,5,4,3,2)[i])
    digito1 = 11 - (soma % 11)
    if digito1 > 9:
        digito1 = 0
    soma = 0
    for i in range(13):
        soma += int(cnpj[i]) * ((6,5,4,3,2,9,8,7,6,5,4,3,2)[i])
    digito2 = 11 - (soma % 11)
    if digito2 > 9:
        digito2 = 0
    # cnpj[-2:] == f"{digito1}{digito2}"
    return True


def get_address(cep):
    address = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    if address.status_code in [200, 201] :
        return json.loads(address.text)
    else: 
        return (address.status_code,address.text)


def send_email(sender_email: str, receiver_email: str, subject: str, body: str, attachment_path: str = None, smtp_server: str = 'smtp.gmail.com', smtp_port: int = 587, username: str = None, password: str = None):
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    
    msg.attach(MIMEText(body, 'plain'))

    
    if attachment_path is not None:
        with open(attachment_path, 'rb') as f:
            attachment = MIMEApplication(f.read(), _subtype='pdf')
            attachment.add_header('Content-Disposition', 'attachment', filename=f.name)
            msg.attach(attachment)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(username, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

def process_data(db,j_data):
    not_updated = []
    update_list = []
    partener_list = []
    pattern = r"\(\d{2}\)\s\d{5}-\d{4}"
    email_pattern = r"[^@]+@[^@]+\.[^@]+"
    cep_pattern = r"\d{5}-\d{3}"
    for i in j_data : 
        if valida_cnpj(i["CNPJ"]) \
            and re.match(pattern, i["Telefone"]) \
            and re.match(email_pattern, i["Email"]) \
            and re.match(cep_pattern, i["CEP"]):
                i["endereco"] = get_address(i["CEP"])
                update_list.append(i)
                partener = parteners.Partener(
                                              name = i["Nome Fantasia"],
                                              razao_social = i["Razão Social"],
                                              cnpj = i["CNPJ"],
                                              email = i["Email"],
                                              phone_number=i["Telefone"],
                                              address = get_address(i["CEP"]))
                partener_list.append(partener)
        else :
            error_list = []
            if not valida_cnpj(i["CNPJ"]):
                error_list.append("CNPJ invalido")
            if not re.match(pattern, i["Telefone"]):
                error_list.append("Telefone invalido")
            if not re.match(email_pattern, i["Email"]):
                error_list.append("Email invalido")
            if not re.match(cep_pattern, i["CEP"]):
                error_list.append("CEP invalido")

            i["error"] = {"error" : error_list}
            not_updated.append(i)
    updated_data = crud.update_partener(db=db, data=partener_list)
    #email sender nao formatado
    # if len(updated_data) > 0  :
    #     for i in updated_data:
    #         send_email(sender_email="teste@gmail.com",
    #                     receiver_email= i,
    #                     subject= "Bem vindo",
    #                     body= "",
    #                     attachment_path = None,
    #                     smtp_server= 'smtp.gmail.com',
    #                     smtp_port= 587,
    #                     username= "user",
    #                     password= "pass")

    return {"updated_inserted":update_list, "Errors_notinserted":not_updated}

