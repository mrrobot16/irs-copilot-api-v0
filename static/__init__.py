from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

def configure_static_files(app: FastAPI):
    app.mount("/static", StaticFiles(directory="static"), name="static")
    templates = Jinja2Templates(directory="templates")
    @app.get("/web")
    async def read_root(request: Request):
        return templates.TemplateResponse("index.html", {"request": request, "title": "FastAPI Tutorial Home Page"})

