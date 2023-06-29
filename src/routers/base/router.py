from src.routers.base.app import AmaterasuApp

class BaseRouter:

    app = AmaterasuApp.get_app()

    @classmethod
    def register_routers(cls):
        cls.__include_xx_router()

        return cls.app


    @classmethod
    def __include_xx_router(cls):
        pass