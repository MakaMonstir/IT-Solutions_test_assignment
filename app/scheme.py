from pydantic import BaseModel

class AdScheme(BaseModel):
    ad_id: int
    title: str
    author: str
    views: int
    position: int

    class Config:
        orm_mode = True