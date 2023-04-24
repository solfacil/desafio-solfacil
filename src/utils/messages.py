import json

from src.utils.string_to_snake import snake_case


class Message:
    def __init__(self, message_type="exception") -> None:
        path_messages = "src/config/messages.json"
        self.messages = json.load(open(path_messages, "r"))
        self.message_type = message_type

    def is_valid_message_key(self, message_key):
        return message_key in self.messages[self.message_type]

    def get(self, message_key):
        message_key = snake_case(message_key)
        if self.is_valid_message_key(message_key):
            return self.messages[self.message_type][message_key]
        else:
            return self.messages["exception"]["message_not_found"]
