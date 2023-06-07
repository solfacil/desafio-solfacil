from pydantic import BaseModel, Field


class Parceiro(BaseModel):
    id: int | None = Field(default=None)
    cnpj: str = Field(..., min_length=14, max_length=14, example="00000000000000")
    razao_social: str = Field(..., max_length=150, example="Razão Social")
    nome_fantasia: str = Field(..., max_length=80, example="Nome Fantasia")
    telefone: str = Field(..., min_length=11, max_length=12, example="11966076344")
    email: str = Field(..., example="email@email.com")
    cep: str = Field(..., min_length=8, max_length=8, example="00000000")
    cidade: str | None = Field(default=None)
    estado: str | None = Field(default=None)
