from app import Utils

def test_check_cnpj():
    cnpj_1 = "16.470.954/0001-06"
    cnpj_2 = "19.478.819/0001-97"
    cnpj_3 = "12.473.742/0001-13"
    cnpj_4 = "214.004.920-92"
    cnpj_5 = "22783-115"

    assert Utils.check_cnpj(cnpj_1) is True
    assert Utils.check_cnpj(cnpj_2) is True
    assert Utils.check_cnpj(cnpj_3) is True
    assert Utils.check_cnpj(cnpj_4) is False
    assert Utils.check_cnpj(cnpj_5) is False

def test_check_email():
    email_1 = "atendimento@soleterno.com"
    email_2 = "atendimentosoldamanha.com"
    email_3 = "atendimentosolforte.com"
    email_4 = "atendimento@soleterno.com"
    email_5 = "atendimento@solenergia.com"

    assert Utils.check_email(email_1) is True
    assert Utils.check_email(email_2) is False
    assert Utils.check_email(email_3) is False
    assert Utils.check_email(email_4) is True
    assert Utils.check_email(email_5) is True

def test_check_telefone():
    telefone_1 = "(21) 98207-9901"
    telefone_2 = "(21) 98207-9902"
    telefone_3 = "21982079903"
    telefone_4 = "(21) 8207-9902"
    telefone_5 = ""

    assert Utils.check_telefone(telefone_1) is True
    assert Utils.check_telefone(telefone_2) is True
    assert Utils.check_telefone(telefone_3) is False
    assert Utils.check_telefone(telefone_4) is True
    assert Utils.check_telefone(telefone_5) is False

def test_get_address_by_cep():
    cep_1 = "22783115"
    cep_2 = "22783-115"
    cep_3 = "123"

    assert Utils.get_address_by_cep(cep_1)["uf"] is not "RJ"
    assert Utils.get_address_by_cep(cep_2) is not {}
    assert Utils.get_address_by_cep(cep_3) is None
