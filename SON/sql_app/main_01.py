from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine
import os
from fastapi.responses import FileResponse

app = FastAPI()



app.mount("/css", StaticFiles(directory="css"), name="css")
app.mount("/js", StaticFiles(directory="js"), name="js")
app.mount("/icon", StaticFiles(directory="icon"), name="icon")
app.mount("/Logo", StaticFiles(directory="Logo"), name="Logo")
app.mount("/photo", StaticFiles(directory="photo"), name="photo")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")
app.mount("/images", StaticFiles(directory="C:/dev/workspace/fast_api_test/2024_SPARCS_relog/sql_app/templates/images"), name="images")



@app.get("/image_display")
def index():
   return FileResponse("C:/dev/workspace/fast_api_test/2024_SPARCS_relog/sql_app/templates/image_display.html")


@app.get("/video_display")
def video():
   return FileResponse("C:/dev/workspace/fast_api_test/2024_SPARCS_relog/sql_app/templates/video_display.html")



