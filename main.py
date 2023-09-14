import uvicorn

from src.routers.base.router import BaseRouter

app = BaseRouter.register_routers()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)

