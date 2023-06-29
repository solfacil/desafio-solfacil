from http import HTTPStatus

from fastapi import FastAPI, Request

from src.routers.base.app import AmaterasuApp

class BaseRouter:

    app = AmaterasuApp.get_app()

    @classmethod
    def __include_xx_router(cls):
        pass