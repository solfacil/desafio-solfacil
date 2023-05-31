from pydantic import BaseModel, UUID4


class Parceiro(BaseModel):
    """Define o modelo do Parceiro"""
    id_: UUID4
    cnpj: str
    razao_social: str
    nome_fantasia: str
    telefone: str
    email: str
    cidade: str
    estado: str
    cep: str

    class Config:
        orm_mode = True
