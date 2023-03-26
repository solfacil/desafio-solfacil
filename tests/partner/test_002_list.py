from fastapi.testclient import TestClient
from loguru import logger  # noqa: F401

from src.app.database import DB
from src.app.main import Base as DBBase
from src.app.main import app, db_infos

from ..helpers import PartnerFactory

client = TestClient(app)


class TestListPartners:

    @classmethod
    def setup_class(cls):

        DB.connect(**db_infos)
        DBBase.metadata.create_all(DB.engine)

        # --------------------------------------------------
        cls.client = TestClient(app)
        cls.population_size = 20
        cls.population: list[PartnerFactory] = []
        for _ in range(cls.population_size):
            partner = PartnerFactory.generate()
            cls.population.append(partner)
            response = cls.client.post("/api/partner/create", json=partner.body)
            assert response.status_code == 201

        # --------------------------------------------------

        cls.inserted_cnpjs = [i.clean_cnpj for i in cls.population]
        return

    @classmethod
    def teardown_class(cls):
        DBBase.metadata.drop_all(DB.engine)
        return

    def setup_method(self):
        ...

    def teardown_method(self):
        ...

    def test_slice_list(self):
        params = {'page': 1, 'size': 5}
        response = client.get("/api/partner/list", params=params)
        assert response.status_code == 200
        assert int(response.json()['pages']) == 4
        assert len(response.json()['items']) == 5
        return

    def test_full_population(self):
        params = {'page': 1, 'size': self.population_size}
        response = client.get("api/partner/list", params=params)
        assert response.status_code == 200
        assert all([True if item['cnpj'] in self.inserted_cnpjs else False for item in response.json()['items']]) is True
        return
