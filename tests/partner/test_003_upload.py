from fastapi.testclient import TestClient
from loguru import logger  # noqa: F401
from unidecode import unidecode

from src.app.database import DB
from src.app.main import Base as DBBase
from src.app.main import Partner, PartnerAddress, PartnerContact, app, db_infos

from ..helpers import PartnerFactory


class TestUpload:

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

    def test_uploadfile_wrong_field_name(self):
        """Upload a file with wrong header names"""
        partner = PartnerFactory.generate()

        data = f"""CNPJ,RazãosSocial,Nome aantasia,Telefone,Email, CEP
{partner.cnpj},{partner.razao_social},{partner.nome_fantasia},{partner.telefone},{partner.email},{partner.cep}"""

        # --------------------------------------------------

        files = {"file": ('file.csv', data)}

        response = self.client.post("/api/partner/insert_update_by_csv", files=files)

        # --------------------------------------------------

        assert response.status_code == 202

        js = response.json()
        errors = js['errors']

        assert errors == [
            {
                'KeyError':
                    "Couldn't find any value for 'razao_social' with '['Razão Social', 'razão social']'. Available names are: '['cnpj', 'razãossocial', 'nome aantasia', 'telefone', 'email', 'cep']'"
            }
        ]

        return

    def test_uploadfile_unknow_field(self):
        """Upload a file with unknowfield, unused, at the end of headers
        the endpoint should ignore the field and insert the data correctly"""
        partner = PartnerFactory.generate()

        data = f"""CNPJ,Razão Social,Nome Fantasia,Telefone,Email, CEP, UNKNOWFIELD
{partner.cnpj},{partner.razao_social},{partner.nome_fantasia},{partner.telefone},{partner.email},{partner.cep}, 'unknowfield'"""

        # --------------------------------------------------

        files = {"file": ('file.csv', data)}

        response = self.client.post("/api/partner/insert_update_by_csv", files=files)

        # --------------------------------------------------

        assert response.status_code == 202

        js = response.json()
        success = js['loaded']
        errors = js['errors']

        assert errors == []

        for added in success:
            assert added['cnpj'] == partner.clean_cnpj

        # --------------------------------------------------

        with DB.get_session().begin() as session:
            in_db_partner = session.query(Partner).filter_by(cnpj=partner.clean_cnpj).first()
            assert in_db_partner is not None
            assert in_db_partner.nome_fantasia == partner.nome_fantasia
            assert in_db_partner.razao_social == partner.razao_social
        return

    def test_uploadfile_unknow_middle_field(self):
        """Upload a file with unknowfield, unused, in the middle of know ones
        the endpoint should ignore the field and insert the data correctly"""

        partner = PartnerFactory.generate()

        data = f"""CNPJ,Razão Social,Nome Fantasia,Telefone,Email, UNKNOWFIELD, CEP
{partner.cnpj},{partner.razao_social},{partner.nome_fantasia},{partner.telefone},{partner.email},'unknowfield',{partner.cep}"""

        # --------------------------------------------------

        files = {"file": ('file.csv', data)}
        response = self.client.post("/api/partner/insert_update_by_csv", files=files)

        # --------------------------------------------------

        assert response.status_code == 202

        js = response.json()
        success = js['loaded']

        for added in success:
            assert added['cnpj'] == partner.clean_cnpj

        # --------------------------------------------------

        with DB.get_session().begin() as session:
            in_db_partner = session.query(Partner).filter_by(cnpj=partner.clean_cnpj).first()
            assert in_db_partner is not None
            assert in_db_partner.nome_fantasia == partner.nome_fantasia
            assert in_db_partner.razao_social == partner.razao_social
        return

    def test_uploadfile_ok(self):
        """Upload a know file that must work"""

        data = """CNPJ,Razão Social,Nome Fantasia,Telefone,Email, CEP
16.470.954/0001-06,Sol Eterno,Sol Eterno LTDA,(21) 98207-9901,atendimento@soleterno.com,22783-115
19.478.819/0001-97,Sol da Manhã,Sol da Manhã LTDA,(21) 98207-9902,atendimentosoldamanha.com,69314-690
12.473.742/0001-13,Sol Forte,Sol Forte LTDA,21982079903,atendimentosolforte.com,84043-150
214.004.920-92,Sol Brilhante,,(21) 8207-9902,atendimento@soleterno.com,57071-186
22783-115,Sol Energia,Sol Energia LTDA,,atendimento@solenergia.com,12900-303"""

        # --------------------------------------------------

        files = {"file": ('file.csv', data)}
        response = self.client.post("/api/partner/insert_update_by_csv", files=files)

        # --------------------------------------------------

        assert response.status_code == 202

        js = response.json()
        success = js['loaded']
        errors = js['errors']

        expected_success = [{'cnpj': '16470954000106'}, {'cnpj': '19478819000197'}, {'cnpj': '12473742000113'}]  # yapf: disabled
        expect_errors = [
            {
                'loc': ['cnpj'],
                'msg': "The CNPJ '21400492092' is invalid.",
                'type': 'value_error'
            }, {
                'loc': ['cnpj'],
                'msg': "The CNPJ '22783115' is invalid.",
                'type': 'value_error'
            }
        ]  # yapf: disabled

        # --------------------------------------------------

        assert [d['cnpj'] for d in success] == [d['cnpj'] for d in expected_success]

        assert errors == expect_errors

        # --------------------------------------------------

        with DB.get_session().begin() as session:
            for added in success:
                in_db_partner = session.query(Partner).filter_by(cnpj=added['cnpj']).first()
                assert in_db_partner is not None
                assert unidecode(in_db_partner.cnpj) == unidecode(added['cnpj'])
                assert unidecode(in_db_partner.nome_fantasia) == unidecode(added['nome_fantasia'])
                assert unidecode(in_db_partner.razao_social) == unidecode(added['razao_social'])

                in_db_address = session.query(PartnerAddress).filter_by(partner_id=in_db_partner.id).first()
                assert in_db_address is not None

                in_db_contact = session.query(PartnerContact).filter_by(partner_id=in_db_partner.id).first()
                assert in_db_contact is not None
        return

    def test_update_entry(self):
        """after inserting an entry with an CSV, uploading the same csv with other values should change the DB"""

        partner = PartnerFactory.generate()

        data = f"""CNPJ,Razão Social,Nome Fantasia,Telefone,Email, CEP
{partner.cnpj},{partner.razao_social},{partner.nome_fantasia},{partner.telefone},{partner.email},{partner.cep}"""

        # --------------------------------------------------

        files = {"file": ('file.csv', data)}
        response = self.client.post("/api/partner/insert_update_by_csv", files=files)

        # --------------------------------------------------

        assert response.status_code == 202

        js = response.json()
        success = js['loaded']

        with DB.get_session().begin() as session:
            for added in success:
                in_db_partner = session.query(Partner).filter_by(cnpj=partner.clean_cnpj).first()
                assert in_db_partner is not None
                assert in_db_partner.nome_fantasia == partner.nome_fantasia
                assert in_db_partner.razao_social == partner.razao_social

        # --------------------------------------------------
        novo_nome_razao_social = 'novo_nome_razao_social'
        novo_nome_fantasia = 'novo_nome_fantasia'

        data = f"""CNPJ,Razão Social,Nome Fantasia,Telefone,Email, CEP
{partner.cnpj},{novo_nome_razao_social},{novo_nome_fantasia},{partner.telefone},{partner.email},{partner.cep}"""
        files = {"file": ('file.csv', data)}

        response = self.client.post("/api/partner/insert_update_by_csv", files=files)
        assert response.status_code == 202

        js = response.json()
        success = js['loaded']

        for added in success:
            assert added['cnpj'] == partner.clean_cnpj

        with DB.get_session().begin() as session:
            in_db_partner = session.query(Partner).filter_by(cnpj=partner.clean_cnpj).first()
            assert in_db_partner.razao_social == novo_nome_razao_social
            assert in_db_partner.nome_fantasia == novo_nome_fantasia
        return

    def test_uploadfile_random_data(self):

        population_size = 20

        data = "CNPJ,Razão Social,Nome Fantasia,Telefone,Email, CEP"

        for _ in range(population_size):
            partner = PartnerFactory.generate()
            data += f"\n{partner.cnpj},{partner.razao_social},{partner.nome_fantasia},{partner.telefone},{partner.email},{partner.cep}"

        files = {"file": ('file.csv', data)}

        response = self.client.post("/api/partner/insert_update_by_csv", files=files)
        assert response.status_code == 202
        return
