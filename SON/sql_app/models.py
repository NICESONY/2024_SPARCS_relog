from sqlalchemy import Column, Integer, String
from .database import Base

class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    photo_url = Column(String(255), nullable=True)
    date = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    user_id = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    hashtag = Column(String(255), nullable=False)
    content = Column(String(255), nullable=False)


# 이미지 post를 위해서 
# Updated model for storing image file paths
class ImageModel(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, index=True)
    file_path = Column(String(255), index=True)  # Specified length of 255 for the VARCHAR column