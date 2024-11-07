import requests
from sqlalchemy.orm import Session
from db import SearchHistory

API_URL = "https://the-one-api.dev/v2"
API_KEY = "f9fmNZ7im1abv9RlF-77"

def get_movies():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(f"{API_URL}/movie", headers=headers)
    return response.json()

def log_search(db: Session, query: str, response: str):
    history_entry = SearchHistory(query=query, response=response)
    db.add(history_entry)
    db.commit()
    db.refresh(history_entry)
    return history_entry

def get_search_history(db: Session):
    return db.query(SearchHistory).all()
