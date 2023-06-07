import logging
from asyncio import sleep

from app.application.usecases.sender.abstract_sender import AbstractSender


class EmailSender(AbstractSender):

    def __init__(self):
        ...

    async def send(self, recipient: str, subject: str, body: str) -> None:
        logging.info(f"Sending email to {recipient} with subject {subject} and body {body}")
        await sleep(1)
        logging.info(f"Email sent to {recipient} with subject {subject} and body {body}")
