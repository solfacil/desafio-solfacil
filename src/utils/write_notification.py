def send_email(parceiro):
    message = f'Olá, {parceiro["nome_fantasia"]}. Seja bem vindo ao sistema da Solfácil'
    with open("welcome_message_to_parceiros.txt", mode="a") as email_file:
        content = f'notification for {parceiro["email"]}: {message}\n'
        email_file.write(content)
