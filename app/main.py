from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, init_db, database
from scheme import AdScheme
from models import Ad

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI(title='Advertisments')

@app.on_event("startup")
async def startup():
    await database.connect()
    init_db()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/ad/{ad_id}", response_model=AdScheme)
async def read_ad(ad_id: int, db: Session = Depends(get_db)):
    ad = db.query(Ad).filter(Ad.id == ad_id).first()
    if ad is None:
        raise HTTPException(status_code=404, detail="This ad don't exist")
    return ad

@app.get("/ad/", response_model=List[AdScheme])
async def read_ad(ad_id: int, db: Session = Depends(get_db)):
    ads = db.query(Ad).limit(10)
    if ads is None:
        raise HTTPException(status_code=404, detail="No ads exists")
    return ads
