import re


def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)


def is_cnpj_valid(cnpj):
    # Regular expression pattern for CNPJ format validation
    pattern = r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$'

    # Use the pattern to match the CNPJ format
    if re.match(pattern, cnpj):
        return True
    else:
        return False


def is_email_valid(email):
    # Regular expression pattern for email validation
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    # Use the pattern to match the email address
    if re.match(pattern, email):
        return True
    else:
        return False
