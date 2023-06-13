import psycopg2
import os
from dotenv import load_dotenv

DATABASE_CONN = None
def get_conn():
    load_dotenv()
    global DATABASE_CONN
    if DATABASE_CONN is None:
        DATABASE_CONN = psycopg2.connect(
            host=os.getenv('DATABASE_HOST'),
            port=os.getenv('DATABASE_PORT'),
            database=os.getenv('DATABASE'),
            user=os.getenv('DATABASE_USER'),
            password=os.getenv('DATABASE_PASSWORD')
        )
    return DATABASE_CONN


def upsert_cep(data):
    db = get_conn()
    cursor = db.cursor()

    sql = """
        INSERT INTO address (CEP, street, complement, district, city, uf, city_ibge)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (CEP) DO UPDATE
        SET street = EXCLUDED.street,
        complement = EXCLUDED.complement,
        district = EXCLUDED.district,
        city = EXCLUDED.city,
        uf = EXCLUDED.uf,
        city_ibge = EXCLUDED.city_ibge
    """

    values = [(item['cep'], item['logradouro'], item['complemento'], item['bairro'], item['localidade'], item['uf'],  item['ibge']) for item in data]
    cursor.executemany(sql, tuple(values))

    db.commit()
    cursor.close()

def upsert_partners(data):
    db = get_conn()
    print(db)
    cursor = db.cursor()

    sql = """
        INSERT INTO partners (cnpj, registered_name, fantasy_name, telephone, email, cep)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (cnpj) DO UPDATE
        SET registered_name = EXCLUDED.registered_name,
        fantasy_name = EXCLUDED.fantasy_name,
        telephone = EXCLUDED.telephone,
        email = EXCLUDED.email,
        cep = EXCLUDED.cep
    """

    values = [(item['CNPJ'], item['Razão Social'], item['Nome Fantasia'], item['Telefone'], item['Email'], item['CEP'] ) for item in data]
    cursor.executemany(sql, tuple(values))
    
    db.commit()
    cursor.close()

def get_users_to_send_emails():
    db = get_conn()
    cursor = db.cursor()

    sql = """
        SELECT fantasy_name, email, cnpj 
        FROM partners 
        WHERE partners.email_has_send IS NOT TRUE
    """
    cursor.execute(sql)

    rows = cursor.fetchall()
    result = []
    columns = ("fantasy_name", "email", "cnpj")
    for row in rows:
        result.append(dict(zip(columns,row)))

    cursor.close()
    return result


def get_all():
    db = get_conn()
    cursor = db.cursor()

    sql = """
    SELECT
        partners.cnpj,
        partners.registered_name,
        partners.fantasy_name,
        partners.telephone,
        partners.email,
        partners.CEP,
        address.city,
        address.uf
    FROM
        partners
    INNER JOIN address 
        ON partners.CEP = address.CEP
    """
    cursor.execute(sql)

    rows = cursor.fetchall()
    result = []
    columns = ("cnpj", "registered_name", "fantasy_name", "telephone", "email", "CEP", "city", "UF")
    for row in rows:
        result.append(dict(zip(columns,row)))

    cursor.close()
    return result

def upsert_email_has_send(data):
    db = get_conn()
    cursor = db.cursor()

    sql = """ 
        UPDATE partners
        SET email_has_send = %s
        WHERE cnpj IN %s
    """

    values = (True, tuple([item["cnpj"] for item in data]))
    cursor.execute(sql, values)
    
    db.commit()
    cursor.close()

def clean_db():
    db = get_conn()
    cursor = db.cursor()
    
    sql = "DELETE FROM address"
    cursor.execute(sql)

    sql = "DELETE FROM partners"
    cursor.execute(sql)
    
    db.commit()
    cursor.close()
