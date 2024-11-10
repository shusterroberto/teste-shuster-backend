from pydantic import BaseModel
from datetime import datetime

class MovieQuery(BaseModel):
    query: str

class SearchHistoryResponse(BaseModel):
    id: int
    query: str
    timestamp: datetime
    response: str
    user: str

    class Config:
        orm_mode = True
