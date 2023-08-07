import logging
import httpx
from rich.console import Console
from rich.logging import RichHandler

console = Console(color_system="256", width=150, style="blue")


def get_logger(module):
    logger = logging.getLogger(module)
    handler = RichHandler(rich_tracebacks=True,
                          console=console, tracebacks_show_locals=True)
    handler.setFormatter(logging.Formatter(
        "%(name)s - [ %(threadName)s:%(funcName)s:%(lineno)d ] - %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger


async def call_external_cep_api(zip_code):
    async with httpx.AsyncClient() as client:
        address = await client.get(f'https://viacep.com.br/ws/{zip_code}/json/')
        address_data = address.json()

    return address_data
