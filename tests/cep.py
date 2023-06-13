from app import cep

def test_get_url():
    result = cep.get_url("12345-123")
    assert result == "https://viacep.com.br/ws/12345-123/json/"
