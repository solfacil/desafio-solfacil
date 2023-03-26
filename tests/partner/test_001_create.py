import random

from fastapi.testclient import TestClient
from loguru import logger  # noqa: F401
from validate_docbr import CNPJ

from src.app.database import DB
from src.app.main import Base as DBBase
from src.app.main import Partner as DBPartner
from src.app.main import app, db_infos

from ..helpers import PartnerFactory


class TestCreate:

    @classmethod
    def setup_class(cls):

        DB.connect(**db_infos)
        DBBase.metadata.create_all(DB.engine)

        cls.client = TestClient(app)
        return

    @classmethod
    def teardown_class(cls):
        DBBase.metadata.drop_all(DB.engine)
        return

    def setup_method(self):
        ...

    def teardown_method(self):
        ...

    def test_create(self):
        partner = PartnerFactory.generate()

        response = self.client.post("/api/partner/create", json=partner.body)
        assert response.status_code == 201

        with DB.get_session().begin() as db:
            in_db_partner = db.query(DBPartner).filter_by(cnpj=partner.clean_cnpj).first()
            assert in_db_partner is not None
            assert in_db_partner.nome_fantasia == partner.nome_fantasia
            assert in_db_partner.razao_social == partner.razao_social
            assert in_db_partner.cnpj == partner.clean_cnpj
        return

    def test_create_invalid_cnpj(self):
        partner = PartnerFactory.generate()

        cnpj = CNPJ()
        while cnpj.validate(partner.clean_cnpj):
            partner.cnpj = f'{random.randint(10, 99)}.{random.randint(100, 999)}.{random.randint(100, 999)}/0001-{random.randint(10, 99)}'

        response = self.client.post("/api/partner/create", json=partner.body)
        assert response.status_code == 422
        assert f"The CNPJ '{partner.clean_cnpj}' is invalid" in response.json()['message']
        return

    def test_create_already_exists(self):
        partner = PartnerFactory.generate()

        response = self.client.post("/api/partner/create", json=partner.body)
        assert response.status_code == 201

        response = self.client.post("/api/partner/create", json=partner.body)
        assert response.status_code == 302
        assert response.text == f"Partner with cnpj '{partner.clean_cnpj}' already exists"
        return

    def test_create_with_viacep_query(self, monkeypatch):
        monkeypatch.setenv("GET_ADDRESS_FROM_VIACEP", "1")
        partner = PartnerFactory.generate()
        partner.cep = '72242-165'

        response = self.client.post("/api/partner/create", json=partner.body)
        assert response.status_code == 201

        with DB.get_session().begin() as db:
            in_db_partner = db.query(DBPartner).filter_by(cnpj=partner.clean_cnpj).first()
            assert in_db_partner is not None
            assert in_db_partner.address.logradouro == 'QNP 27 Conjunto H'
            assert in_db_partner.address.uf == 'DF'
            assert in_db_partner.address.ibge == '5300108'

        monkeypatch.setenv("GET_ADDRESS_FROM_VIACEP", "0")
        return
