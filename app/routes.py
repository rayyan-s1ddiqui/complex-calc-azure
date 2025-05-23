from fastapi import APIRouter, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.calculator import crunch
from app.upload import save_and_ocr

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})

@router.post("/calculate", response_class=HTMLResponse)
async def calculate(request: Request, expression: str = Form(...)):
    result = crunch(expression)
    return templates.TemplateResponse("index.html", {"request": request, "result": result})

@router.post("/upload", response_class=HTMLResponse)
async def upload_image(request: Request, file: UploadFile = File(...)):
    expression = save_and_ocr(file)
    result = crunch(expression)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "expression": expression,
        "result": result
    })