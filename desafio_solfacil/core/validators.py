import re

from django.core.exceptions import ValidationError


def is_valid_cnpj(value):
    cnpj = re.sub(r"[^0-9]", "", str(value)).zfill(14)

    if len(re.sub(r"([0-9])\1+", r"\1", cnpj)) == 1 or len(cnpj) != 14:
        return False

    cnpj = tuple(map(int, cnpj))

    v1, v2 = 0, 0

    v1 = (
        (5 * cnpj[0] + 4 * cnpj[1] + 3 * cnpj[2] + 2 * cnpj[3])
        + (9 * cnpj[4] + 8 * cnpj[5] + 7 * cnpj[6] + 6 * cnpj[7])
        + (5 * cnpj[8] + 4 * cnpj[9] + 3 * cnpj[10] + 2 * cnpj[11])
    ) % 11

    if v1 < 2:
        v1 = 0
    else:
        v1 = 11 - v1

    v2 = (
        (
            (
                6 * cnpj[0]
                + 5 * cnpj[1]
                + 4 * cnpj[2]
                + 3 * cnpj[3]
                + 2 * cnpj[4]
            )
            + (2 * cnpj[4] + 9 * cnpj[5] + 8 * cnpj[6] + 7 * cnpj[7])
            + (6 * cnpj[8] + 5 * cnpj[9] + 4 * cnpj[10] + 3 * cnpj[11])
        )
        + 2 * v1
    ) % 11
    if v2 < 2:
        v2 = 0
    else:
        v2 = 11 - v2

    if v1 != int(value[-2]) or v2 != int(value[-1]):
        return False

    return True


def is_valid_cpf(value):
    cpf = re.sub(r"[^0-9]", "", str(value)).zfill(11)

    if len(re.sub(r"([0-9])\1+", r"\1", cpf)) == 1:
        return False

    v1, v2 = 0, 0

    for i, d in enumerate(map(int, cpf[:-2][::-1])):
        v1 += d * (9 - (i % 10))
        v2 += d * (9 - ((i + 1) % 10))

    v1 = (v1 % 11) % 10
    v2 = ((v2 + v1 * 9) % 11) % 10

    if v1 != int(cpf[-2]) or v2 != int(cpf[-1]):
        return False

    return False


def validate_cpf(value):
    if not is_valid_cpf(value):
        raise ValidationError("CPF inválido")


def validate_cnpj(value):
    if not is_valid_cnpj(value):
        raise ValidationError("CNPJ inválido")


def validate_cpf_or_cnpj(value):
    if not is_valid_cpf(value) and not is_valid_cnpj(value):
        raise ValidationError("CPF ou CNPJ inválido")
