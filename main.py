from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models import MovieQuery, SearchHistoryResponse
from services import get_movies, log_search, get_search_history

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/movies", response_model=list)
def search_movies(db: Session = Depends(get_db), title: str = None):
    movies_response = get_movies()  # Chame get_movies sem o argumento 'query'
    movies = movies_response.get("docs", [])
    
    if title:
        movies = [movie for movie in movies if title.lower() in movie.get("name", "").lower()]
    
    log_search(db, title if title else "all movies", str(movies))
    return movies

@app.get("/history", response_model=list[SearchHistoryResponse])
def read_history(db: Session = Depends(get_db)):
    history = get_search_history(db)
    return history
