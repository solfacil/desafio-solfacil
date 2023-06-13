def send_email(data):
    for partner in data:
        print("--------------------- new email to send ---------------------")
        print("Mandando email para ", partner['email'])
        print("Seja bem vindo ", partner['fantasy_name'])
        print("\n")