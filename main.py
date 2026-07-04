from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

from projects import PROJECTS

app = FastAPI(title="Álvaro González Sánchez – Portfolio")

BASE_DIR = Path(__file__).parent

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(request, "index.html", {"projects": PROJECTS})


@app.get("/cv")
async def cv_en():
    return FileResponse(BASE_DIR / "static" / "gonzalez-sanchez-cv-en.html", media_type="text/html")


@app.get("/cv/nl")
async def cv_nl():
    return FileResponse(BASE_DIR / "static" / "gonzalez-sanchez-cv-nl.html", media_type="text/html")
