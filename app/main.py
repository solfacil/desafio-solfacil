from fastapi import Request, FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routes import partners

templates = Jinja2Templates(directory="app/templates")

app = FastAPI(version='0.0.1', title='Manage customers API', description='API to manage customers from partners')
app.include_router(partners.router, prefix='/api/v1/partners', tags=['Partners'])
app.mount("/static", StaticFiles(directory="app/templates/static"), name="static")


@app.get("/", summary='Home page', description='HTML form to import customers to partners')
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
