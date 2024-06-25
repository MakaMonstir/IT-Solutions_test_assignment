import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databases import Database
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
