import smtplib
from email.encoders import encode_base64
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Optional

from loguru import logger
from pydantic import FilePath


def send_email(
    *,
    username: str,
    password: str,
    to: list[str],
    html_body: str,
    title: str,
    smtp_host: str = "smtp.gmail.com",
    smtp_port: int = 465,
    attachments: Optional[list[FilePath]] = None,
    cc: Optional[list[str]] = None,
    bcc: Optional[list[str]] = None
):
    """Send an complete email

    Could be sent to many receivers, with or without CC/BCC.

    ---
    ### Example:
    ```
    from email import send_email
    data = {
        'username':'YOUR@EMAIL.COM',
        'password' : 'Y0URP455W0RD',
        'to' : 'RECEIVER@EMAIL.COM',
        'html_body' : 'html body',
        'title' : 'email title',
        'smtp_host' : "smtp.gmail.com",
        'smtp_port' : "465"
    }
    send_email(**data)
    ```
    ---
    """

    if not isinstance(to, list):
        to = [to]

    if not isinstance(smtp_port, int):
        smtp_port = int(smtp_port)

    all_recipients = []
    if cc:
        all_recipients.extend(cc)
    if bcc:
        all_recipients.extend(bcc)
    all_recipients.extend(to)

    # ----------------------------------

    msg = MIMEMultipart('alternative')
    msg['Subject'] = title
    msg['From'] = username
    if cc:
        msg['To'] = ', '.join(to)
    if bcc:
        msg['Cc'] = ', '.join(cc)

    # ----------------------------------

    mime_html_body = MIMEText(html_body, 'html')
    msg.attach(mime_html_body)

    # ----------------------------------
    # Add the attachments
    if attachments:
        for path in attachments:
            part = MIMEBase('application', "octet-stream")
            with open(path, 'rb') as file:
                part.set_payload(file.read())
            encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename="{path.name}"')
            msg.attach(part)

    # ----------------------------------
    # Send the email

    logger.debug(f"Sending email from: '{msg['From']}' to: '{all_recipients}' with server: {smtp_host}:{smtp_port}")

    try:
        with smtplib.SMTP_SSL(smtp_host, smtp_port) as smtp_server:
            smtp_server.login(username, password)
            smtp_server.sendmail(msg['From'], all_recipients, msg.as_string())
    except Exception as e:
        logger.exception(f"Exception '{e}' while sending e-mail!")
        return False

    logger.debug("E-mail sent")
    return True
