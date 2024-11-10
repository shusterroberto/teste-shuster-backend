from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models import SearchHistoryResponse
from services import get_movies, log_search, get_search_history
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Permite a origem do frontend Angular
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os headers
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/movies", response_model=list)
def search_movies(user: str, db: Session = Depends(get_db), title: str = None):
    movies_response = get_movies()
    movies = movies_response.get("docs", [])

    if title:
        movies = [movie for movie in movies if title.lower() in movie.get("name", "").lower()]

    log_search(db, user, title if title else "all movies", str(movies))
    return movies



@app.get("/history", response_model=list[SearchHistoryResponse])
def read_history(db: Session = Depends(get_db)):
    history = get_search_history(db)
    return history
