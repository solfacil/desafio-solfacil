from app import database

def test_upsert_cep():
    data = [{
        "cep": "11111-111",
        "logradouro": "street 123",
        "complemento": "lala",
        "bairro": "Sao Paulo",
        "localidade": "São Paulo",
        "uf": "SP",
        "ibge": "1234567"
    }]
    database.upsert_cep(data)

    db = database.get_conn()
    cursor = db.cursor()
    sql = "SELECT * FROM address"
    cursor.execute(sql)

    rows = cursor.fetchall()
    assert 1 == len(rows)

    database.clean_db()
    cursor.close()

def test_upsert_partners():
    data = [{
        "CNPJ": "12345678901234",
        "Razão Social": "Empresa One",
        "Nome Fantasia": "Empresa One LTDA",
        "Telefone": "(41) 99999-9999",
        "Email": "testando@test.com.br",
        "CEP": "11111-111",
    }]

    database.upsert_partners(data)

    db = database.get_conn()
    cursor = db.cursor()

    sql = """
        SELECT * FROM partners
    """

    cursor.execute(sql)

    rows = cursor.fetchall()
    assert 1 == len(rows)

    database.clean_db()
    cursor.close()

def test_get_users_to_send_emails():
    data = [{
        "CNPJ": "12345678901234",
        "Razão Social": "Empresa One",
        "Nome Fantasia": "Empresa One LTDA",
        "Telefone": "(41) 99999-9999",
        "Email": "testando@test.com.br",
        "CEP": "11111-111",
    }]

    database.upsert_partners(data)
    result = database.get_users_to_send_emails()
    assert 1 == len(result)

    database.clean_db()
