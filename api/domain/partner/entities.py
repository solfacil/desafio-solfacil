from .exceptions import MissingParamError


class Partner:
    id: str
    cnpj: str
    cpf: str
    corporate_name: str
    trading_name: str
    phone: str
    email: str
    cep: str
    uf: str
    city: str

    def __init__(
        self,
        id: str,
        cnpj: str,
        cpf: str,
        corporate_name: str,
        trading_name: str,
        phone: str,
        email: str,
        cep: str,
        uf: str,
        city: str,
    ) -> None:
        self.id = id
        self.cnpj = cnpj
        self.cpf = cpf
        self.corporate_name = corporate_name
        self.trading_name = trading_name
        self.phone = phone
        self.cep = cep
        self.uf = uf
        self.city = city
        self.email = email

    def create_partner(self):
        self.is_valid()

    def is_valid(self):
        required_fields = ["corporate_name", "cep", "email", "cnpj"]
        for field in required_fields:
            if getattr(self, field) is None:
                raise MissingParamError(field)
        if len(self.cnpj) <= 11:
            self.cpf = self.cnpj
            self.cnpj = None
        else:
            self.cpf = None
        return True
