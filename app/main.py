from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes import router

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Mount static if you ever want to serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routes
app.include_router(router)