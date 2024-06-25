from sqlalchemy import Column, Integer, String
from database import Base

class Ad(Base):
    __tablename__ = 'ads'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    views = Column(Integer, default=0)
    position = Column(Integer, default=0)