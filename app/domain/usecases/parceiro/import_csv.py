from io import StringIO
from typing import List, Dict
import re

import pandas as pd
from pandas import Series

from app.application.dtos.parceiro_dto import ParceiroDto
from app.application.ports.parceiro.parceiro_repository import AbstractParceiroRepository
from app.application.usecases.parceiro.abstract_import_csv import AbstractImportCsvUseCase
from app.domain.entities.parceiro.parceiro import Parceiro
from app.infrastructure.integrations.via_cep import ViaCep
from app.domain.usecases.email_sender.email_sender import EmailSender


class ImportCsvUseCase(AbstractImportCsvUseCase):
    def __init__(self, parceiro_repository: AbstractParceiroRepository):
        self.parceiro_repository = parceiro_repository

    def __sanitize_string(self, string: str) -> str:
        # remove special characters using regex
        if not string:
            return ""
        return re.sub(r"[^a-zA-Z0-9]+", "", string)

    def __commit_parceiro(self, parceiro: Parceiro) -> ParceiroDto:
        if parceiro.id:
            return self.parceiro_repository.update(parceiro)
        return self.parceiro_repository.add(parceiro)


    async def __get_parceiro(self, parceiro_row: Series) -> Parceiro:
        parceiro = Parceiro(
            cnpj=self.__sanitize_string(parceiro_row.get('CNPJ')),
            razao_social=parceiro_row.get('Razão Social'),
            nome_fantasia=parceiro_row.get('Nome Fantasia'),
            telefone=self.__sanitize_string(parceiro_row.get('Telefone')),
            email=parceiro_row.get('Email'),
            cep=self.__sanitize_string(parceiro_row.get('CEP')),
        )

        if address := await ViaCep(parceiro.cep).get_address():
            parceiro.cidade = address.get('cidade')
            parceiro.estado = address.get('estado')

        if existing_parceiro := self.parceiro_repository.get_by_cnpj(parceiro.cnpj):
            parceiro.id = existing_parceiro.id

        return parceiro

    async def __send_welcome_email(self, parceiros: List[Parceiro]) -> None:
        for parceiro in parceiros:
            await EmailSender().send(
                recipient=parceiro.email,
                subject=f"Bem vindo {parceiro.nome_fantasia or parceiro.razao_social}",
                body=
                f"Olá {parceiro.nome_fantasia or parceiro.razao_social}, seja bem vindo ao nosso sistema!",
            )

    async def execute(self, csv_content: str) -> Dict[str, List[ParceiroDto]]:
        df = pd.read_csv(StringIO(csv_content))

        parceiros_to_process = []
        for _, row in df.iterrows():
            parceiros_to_process.append(await self.__get_parceiro(row))

        parceiros = {"created": [], "updated": []}
        with self.parceiro_repository.begin_transaction():
            for parceiro in parceiros_to_process:
                if parceiro.id:
                    parceiros["updated"].append(
                        self.parceiro_repository.update(parceiro)
                    )
                else:
                    parceiros["created"].append(
                        self.parceiro_repository.add(parceiro)
                    )
        await self.__send_welcome_email(parceiros["created"])

        return parceiros
