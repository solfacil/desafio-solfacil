from pydantic import BaseModel, Field


class ParceiroDto(BaseModel):
    id: int | None = Field(...)
    cnpj: str
    razao_social: str
    nome_fantasia: str
    telefone: str
    email: str
    cep: str
    cidade: str | None = Field(default=None)
    estado: str | None = Field(default=None)
