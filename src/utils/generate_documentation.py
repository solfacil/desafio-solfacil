import json

from fastapi.openapi.utils import get_openapi

from src.main import app


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Your API Title",
        version="1.0.0",
        description="Your API Description",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


openapi_schema = custom_openapi()

with open("docs/openapi.json", "w") as file:
    json.dump(openapi_schema, file)
