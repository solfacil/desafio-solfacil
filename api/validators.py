from validate_docbr import CNPJ


def validate_cnpj(cnpj):
    cnpj_validate = CNPJ()
    if not cnpj_validate.validate(cnpj):
       raise ValueError('CNPJ inválido')


def validate_cep(cep):
    if len(cep) != 8:
        raise ValueError('CEP inválido')


def validate_telefone(telefone):
    if len(telefone) != 11:
        raise ValueError('Telefone inválido')


def validate_razao_social(razao_social):
    if not razao_social:
        raise ValueError('Razão social inválido')
