from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Ad(Base):
    __tablename__ = 'ads'

    ad_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    views = Column(Integer, default=0)
    position = Column(Integer, default=0)