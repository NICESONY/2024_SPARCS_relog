# 필요한 라이브러리 import하기
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql

# pymysql을 MySQLdb로 설치하기
pymysql.install_as_MySQLdb()

# SQLAlchemy 사용할 DB URL 생성하기
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:11111111@ls-f5492fc3bff8be679d69c95f451ce31a484356aa.ctawq4asic5c.ap-northeast-2.rds.amazonaws.com:3306/dbsbb"

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:11111111@localhost:3306/MySQL"

# SQLAlchemy engine 생성하기
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# DB 세션 생성하기
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class 생성하기
Base = declarative_base()
