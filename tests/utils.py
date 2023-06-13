from app import utils

def test_validate_email():
  result = utils.validate_email("test@test.com.br")
  assert result == True
  
  result = utils.validate_email("test@test")
  assert result == False
  
  result = utils.validate_email("test.test.com.br")
  assert result == False
  
  result = utils.validate_email("test")
  assert result == False

def test_validate_cnpj():
  result = utils.validate_cnpj("45.217.565/0001-63")
  assert result == True
  
  result = utils.validate_cnpj("test@test")
  assert result == False
  
  result = utils.validate_cnpj("123.456.789-01")
  assert result == False
  
  result = utils.validate_cnpj("12361739612983291387219")
  assert result == False

def test_parse_cnpj():
  result = utils.parse_cnpj("45.217.565/0001-63")
  assert result == "45217565000163"

def test_parse_phone():
  result = utils.parse_phone("(21) 99999-9999")
  assert result == "21999999999"

