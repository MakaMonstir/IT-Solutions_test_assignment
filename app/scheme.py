from pydantic import BaseModel

class AdScheme(BaseModel):
    id: int
    title: str
    author: str
    views: int
    position: int

    class Config:
        orm_mode = True