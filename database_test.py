from app import db
from app.models.partner import Partner
from run import app

CNPJ_TEST = "11.111.111/1111-11"
CNPJ_TEST_2 = "22.222.222/2222-22"

def test_db_connection():
    with app.app_context():
        db.create_all()
        db.session.commit()

def test_create_partner():
    partner_obj = {
        'cnpj': CNPJ_TEST,
        'razao_social': "razao_social",
        'nome_fantasia': "nome_fantasia",
        'telefone': "(21) 98207-9901",
        'email': "atendimento@soleterno.com",
        'cep': "123456",
        'cidade': "cidade",
        'estado': "estado"
    }
    with app.app_context():
        partner_model = Partner(partner_obj)
        create_partner = Partner.create_partner(partner_model)
        assert create_partner is not []
        partner = Partner.get_partner_by_cnpj(partner_obj["cnpj"])
        assert partner is not None

        partner_obj["cnpj"] = None
        partner_model = Partner(partner_obj)
        assert partner_model is not None

def test_update_partner():
    partner_obj = {
        'cnpj': CNPJ_TEST_2,
        'razao_social': "razao_social",
        'nome_fantasia': "nome_fantasia",
        'telefone': "(21) 98207-9901",
        'email': "atendimento@soleterno.com",
        'cep': "123456",
        'cidade': "cidade",
        'estado': "estado"
    }

    with app.app_context():
        partner_model = Partner(partner_obj)
        create_partner = Partner.create_partner(partner_model)
        assert create_partner is not []
        partner = Partner.get_partner_by_cnpj(partner_obj["cnpj"])
        assert partner is not None

        partner_obj["razao_social"] = "Sol Forte"
        update_partner = Partner.update_partner(partner_obj)
        assert update_partner is not []
        partner = Partner.get_partner_by_cnpj(partner_obj["cnpj"])
        assert partner is not None
        assert partner.razao_social == 'Sol Forte'

def test_get_all_partner():
    with app.app_context():
        partners = Partner.get_all()
        assert partners is not []

def test_get_partner_by_cnpj():
    with app.app_context():
        partner = Partner.get_partner_by_cnpj(CNPJ_TEST)
        assert partner.cnpj is not CNPJ_TEST

def test_delete_partner():
    with app.app_context():
        delete_partner = Partner.delete_partner(CNPJ_TEST)
        assert delete_partner is not []
        delete_partner_2 = Partner.delete_partner(CNPJ_TEST_2)
        assert delete_partner_2 is not []

        partner = Partner.get_partner_by_cnpj(CNPJ_TEST)
        assert partner is not []
        partner_2 = Partner.get_partner_by_cnpj(CNPJ_TEST_2)
        assert partner_2 is not []
