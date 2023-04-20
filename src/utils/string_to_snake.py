import re

from unidecode import unidecode


def snake_case(string):
    string = unidecode(string.strip())
    string = re.sub(r"\W+", "_", string)
    return string.lower()
