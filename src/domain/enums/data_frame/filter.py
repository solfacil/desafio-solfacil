from strenum import StrEnum

class ColumnsName(StrEnum):
    CNPJ = 'cnpj'
    COMPANY_NAME = 'company_name'
    FANTASY_ANME = 'fantasy_name'
    PHONE = 'phone'
    EMAIL = 'email'
    ZIPCODE = 'zipcode'


class CnpjQuery(StrEnum):
    equal_14_digits = 'cnpj.str.len() == 14'
    not_equal_14_digits = 'cnpj.str.len() != 14'
