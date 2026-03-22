from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI(title="Álvaro González Sánchez – Portfolio")

BASE_DIR = Path(__file__).parent

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/cv")
async def download_cv():
    cv_path = BASE_DIR / "static" / "gonzalez-sanchez-cv.pdf"
    return FileResponse(
        cv_path,
        media_type="application/pdf",
        filename="gonzalez-sanchez-cv.pdf",
        headers={"Content-Disposition": "attachment; filename=gonzalez-sanchez-cv.pdf"},
    )
