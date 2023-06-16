import logging
from rich.console import Console
from rich.logging import RichHandler

console = Console(color_system="256", width=150, style="blue")

def get_logger(module):
    logger = logging.getLogger(module)
    handler = RichHandler(rich_tracebacks=True, console=console, tracebacks_show_locals=True)
    handler.setFormatter(logging.Formatter("%(name)s - [ %(threadName)s:%(funcName)s:%(lineno)d ] - %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger