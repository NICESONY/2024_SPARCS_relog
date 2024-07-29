from fastapi import FastAPI
app = FastAPI()

# 다른 파일 불러오기
from fastapi.staticfiles import StaticFiles

#fast_api test
## HTML 파일을 띄우고 싶을때 사용

from fastapi.responses import FileResponse



app.mount("/assets", StaticFiles(directory="assets"), name="assets")
app.mount("/css", StaticFiles(directory="css"), name="css")
app.mount("/js", StaticFiles(directory="js"), name="js")



@app.get("/")
def resume():
   return FileResponse("index.html")





################유저에게 데이터를 받기 위한 방법#########


from pydantic import BaseModel

class Model(BaseModel):
   name : str  ## 변수에 타입을 지정할 수 있음
   phone : int


@app.post("/send")
def send(data : Model):
    print(data)
    return "전송완료"

    # test