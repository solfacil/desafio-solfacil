import contextlib
import logging
from typing import Optional

from app.application.dtos.parceiro_dto import ParceiroDto
from app.application.ports.parceiro.parceiro_repository import AbstractParceiroRepository
from app.domain.entities.parceiro.parceiro import Parceiro
from app.infrastructure.database.sqlalchemy.models import ParceiroModel
from app.infrastructure.database.sqlalchemy.session import get_db, get_session


class SqlAlchemyParceiroRepository(AbstractParceiroRepository):

    def __init__(self):
        self.session = None

    @contextlib.contextmanager
    def begin_transaction(self):
        self.session = get_session()
        try:
            yield self.session
            self.session.commit()
        except Exception as err:
            logging.error(err)
            self.session.rollback()
            raise err
        finally:
            if getattr(self.session, "is_active", False):
                self.session.close()

    @contextlib.contextmanager
    def __make_session(self):
        if not self.session or not self.session.is_active:
            with get_db() as session:
                self.session = session
                yield self.session
        else:
            yield self.session

    def add(self, parceiro: Parceiro) -> ParceiroDto:
        db_parceiro = ParceiroModel(**parceiro.dict())
        self.session.add(db_parceiro)
        return ParceiroDto(**db_parceiro.__dict__)

    def get_by_cnpj(self, cnpj: str) -> Optional[ParceiroDto]:
        with self.__make_session() as session:
            db_parceiro = session.query(
                ParceiroModel
            ).filter(
                ParceiroModel.cnpj == cnpj
            ).first()
        return ParceiroDto(**db_parceiro.__dict__) if db_parceiro else None

    def update(self, parceiro: Parceiro) -> ParceiroDto:
        with self.__make_session() as session:
            db_parceiro = session.query(
                ParceiroModel
            ).filter(
                ParceiroModel.id == parceiro.id
            ).first()
        if db_parceiro:
            for key, value in parceiro.dict().items():
                setattr(db_parceiro, key, value)
        return ParceiroDto(**db_parceiro.__dict__)

    def get_all(self) -> list[ParceiroDto]:
        with self.__make_session():
            db_parceiros = self.session.query(ParceiroModel).all()
        return [ParceiroDto(**db_parceiro.__dict__) for db_parceiro in db_parceiros]

    def delete(self, parceiro_id: int) -> None:
        with self.__make_session() as session:
            if db_parceiro := session.query(ParceiroModel).filter(
                    ParceiroModel.id == parceiro_id
            ).first():
                session.delete(db_parceiro)
                session.commit()

    def get_by_id(self, parceiro_id: int) -> Optional[ParceiroDto]:
        with self.__make_session() as session:
            db_parceiro = session.query(ParceiroModel).filter(
                ParceiroModel.id == parceiro_id
            ).first()
            return ParceiroDto(**db_parceiro.__dict__) if db_parceiro else None

    def get_by_email(self, email: str) -> Optional[ParceiroDto]:
        with self.__make_session() as session:
            if db_parceiro := session.query(ParceiroModel).filter(
                ParceiroModel.email == email
            ).first():
                return ParceiroDto(**db_parceiro.__dict__) if db_parceiro else None
