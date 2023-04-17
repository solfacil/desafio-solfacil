from api.domain.partner.entities import Partner


class PartnerDto:
    id: str | None
    cnpj: str | None
    cpf: str | None
    corporate_name: str
    trading_name: str | None
    phone: str | None
    email: str
    cep: str
    uf: str | None
    city: str | None

    def __init__(
        self,
        id: str | None,
        cnpj: str | None,
        cpf: str | None,
        corporate_name: str,
        trading_name: str | None,
        phone: str | None,
        email: str,
        cep: str,
        uf: str | None,
        city: str | None,
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

    def to_domain(self):
        return Partner(
            self.id,
            self.cnpj,
            self.cpf,
            self.corporate_name,
            self.trading_name,
            self.phone,
            self.email,
            self.cep,
            self.uf,
            self.city,
        )

    def to_dto(self, partner: Partner):
        return PartnerDto(
            id=partner.id,
            cnpj=partner.cnpj,
            cpf=partner.cpf,
            corporate_name=partner.corporate_name,
            trading_name=partner.trading_name,
            phone=partner.phone,
            email=partner.email,
            cep=partner.cep,
            uf=partner.uf,
            city=partner.city,
        )
