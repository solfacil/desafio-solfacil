from src.utils.messages import Message


def test_message_initialization():
    message = Message()
    assert isinstance(message, Message)
    assert message.message_type == "exception"


def test_message_initialization_with_custom_type():
    message = Message(message_type="custom")
    assert isinstance(message, Message)
    assert message.message_type == "custom"


def test_is_valid_message_key():
    message = Message()
    assert message.is_valid_message_key("message_not_found")
    assert not message.is_valid_message_key("invalid_key")


def test_get_existing_message_key():
    message = Message()
    result = message.get("message_not_found")
    assert result["detail"] == "A mensagem solicitada não foi encontrada."


def test_get_non_existing_message_key():
    message = Message()
    result = message.get("non_existing_key")
    assert result["detail"] == "A mensagem solicitada não foi encontrada."


def test_get_message_key_with_different_case():
    message = Message()
    result = message.get("MessageNotFound")
    assert result["detail"] == "A mensagem solicitada não foi encontrada."
