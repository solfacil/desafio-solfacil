from src.routers.base.app import AmaterasuApp
from src.routers.partners.router import PartnersRouter


class BaseRouter:
    app = AmaterasuApp.get_app()

    @classmethod
    def register_routers(cls):
        cls.__include_partners_router()

        return cls.app

    @classmethod
    def __include_partners_router(cls):
        router = PartnersRouter.get_partners_router()
        cls.app.include_router(router)
        return cls.app
