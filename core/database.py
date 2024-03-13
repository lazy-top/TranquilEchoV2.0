# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()
DB_USER=os.getenv('DB_USER')
DB_PASS=os.getenv('DB_PASS')
DB_NAME=os.getenv('DB_NAME')
SQLALCHEMY_DATABASE_URL = f'mysql+mysqlconnector://{DB_USER}:{DB_PASS}@localhost:3306/{DB_NAME}?charset=utf8'
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()