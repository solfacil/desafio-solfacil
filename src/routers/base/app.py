from fastapi import FastAPI


class AmaterasuApp:

    __app = FastAPI(title="Amaterasu", description="partners sync")


    @classmethod
    def get_app(cls):
        return cls.__app