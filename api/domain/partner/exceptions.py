class MissingParamError(Exception):
    def __init__(self, param_name):
        super().__init__(f"Missing param: {param_name}")
