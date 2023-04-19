import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.database import Base, crud, get_db, schemas
from src.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./tests/database/test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)


@pytest.fixture(scope="module")
def db() -> Session:
    db = TestingSessionLocal()
    yield db
    db.close()


@pytest.fixture(scope="function")
def client(db) -> TestClient:
    def override_get_db():
        try:
            yield db
        finally:
            db.rollback()

    app.dependency_overrides[get_db] = override_get_db
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as c:
        yield c
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def parceiros_teste(db, client):
    parceiros = [
        {"cnpj": "1234", "cep": "sadsa"},
        {"cnpj": "5678", "cep": "sadsa"},
        {"cnpj": "9101", "cep": "asdsa"},
    ]

    for parceiro in parceiros:
        crud.criar_parceiro(db, schemas.SchemaCriacaoParceiro(**parceiro))
