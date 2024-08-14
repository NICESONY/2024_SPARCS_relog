from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine
import os

from fastapi import File, UploadFile # 사진 업로드를 위해서 추가

from .models import ImageModel  # 이미지 정보를 저장하는 모델




models.Base.metadata.create_all(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory="sql_app/templates")


app.mount("/css", StaticFiles(directory="css"), name="css")
app.mount("/js", StaticFiles(directory="js"), name="js")
app.mount("/icon", StaticFiles(directory="icon"), name="icon")
app.mount("/Logo", StaticFiles(directory="Logo"), name="Logo")
app.mount("/photo", StaticFiles(directory="photo"), name="photo")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")



# 이미지가 저장된 디렉토리 경로 지정
app.mount("/images", StaticFiles(directory="C:/dev/workspace/fast_api_test/2024_SPARCS_relog/sql_app/templates/images"), name="images")



# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



from .models import Record

## 이미지 올리기 위한 getmaping연결
@app.get("/image/{image_id}", response_class=HTMLResponse)
async def get_image(request: Request, image_id: int, db: Session = Depends(get_db)):
    image = db.query(Record).filter(Record.id == image_id).first()
    if image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return templates.TemplateResponse("image_display.html", {"request": request, "image": image})










@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("create_record.html", {"request": request})

@app.post("/records/", response_class=HTMLResponse)
async def create_record(
    request: Request, 
    photo: UploadFile = File(...), 
    date: str = Form(...), 
    location: str = Form(...), 
    user_id: str = Form(...), 
    title: str = Form(...), 
    hashtag: str = Form(...), 
    content: str = Form(...), 
    db: Session = Depends(get_db)
):
    # 파일 저장 로직
    photo_url = f"C:/dev/workspace/fast_api_test/2024_SPARCS_relog/sql_app/templates/images/{photo.filename}"
    with open(photo_url, "wb") as file:
        print(file)
        #change_file_url = file[-1]

        #change_file_url.write(await photo.read())
        file.write(await photo.read())
   
    # 파일 URL이나 저장 경로를 데이터베이스에 저장
    record = schemas.RecordCreate(
        photo_url=photo_url, 
        date=date, 
        location=location, 
        user_id=user_id, 
        title=title, 
        hashtag=hashtag, 
        content=content
    )
    crud.create_record(db=db, record=record)
    records = crud.get_records(db=db)



    print(f"Received photo_url: {photo_url}")


    # main4.py에 출력하기
    with open("sql_app/main4.py", "a", encoding="utf-8") as file:
        file.write("\n# Records Output\n")
        for record in records:
            file.write(f"Date: {record.date}\n")
            file.write(f"Location: {record.location}\n")
            file.write(f"User ID: {record.user_id}\n")
            file.write(f"Title: {record.title}\n")
            file.write(f"Hashtag: {record.hashtag}\n")
            file.write(f"Content: {record.content}\n")
            file.write("------\n")

    return templates.TemplateResponse("records.html", {"request": request, "records": records})
    

@app.get("/records/", response_class=HTMLResponse)
def read_records(request: Request, db: Session = Depends(get_db)):
    records = crud.get_records(db, skip=0, limit=10)
    
    # main4.py에 출력하기
    with open("sql_app/main4.py", "a", encoding="utf-8") as file:
        file.write("\n# Records Output\n")
        for record in records:
            file.write(f"Date: {record.date}\n")
            file.write(f"Location: {record.location}\n")
            file.write(f"User ID: {record.user_id}\n")
            file.write(f"Title: {record.title}\n")
            file.write(f"Hashtag: {record.hashtag}\n")
            file.write(f"Content: {record.content}\n")
            file.write("------\n")

    return templates.TemplateResponse("records.html", {"request": request, "records": records})
