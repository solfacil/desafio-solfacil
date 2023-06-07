from fastapi import FastAPI
from app.interfaces.api.fastapi.routes import parceiro_router
from fastapi.middleware.cors import CORSMiddleware

def get_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
    )
    app.include_router(parceiro_router.router, prefix="/api", tags=["parceiros"])
    return app
