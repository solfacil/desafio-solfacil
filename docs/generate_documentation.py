import json
import subprocess

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


def is_widdershins_installed():
    try:
        process = subprocess.run(
            ["widdershins", "--version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return process.returncode == 0
    except FileNotFoundError:
        return False


def generate_markdown(input_file: str, output_file: str):
    command = f"widdershins {input_file} -o {output_file} \
        --language_tabs 'python:Python' --omitHeader true"
    subprocess.run(command, shell=True, check=True, text=True)


if is_widdershins_installed():
    generate_markdown("docs/openapi.json", "docs/API_DOCUMENTATION.md")
