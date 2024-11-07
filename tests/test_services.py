from sqlalchemy.orm import Session
from ..services import log_search, get_search_history
from ..db import SessionLocal, SearchHistory

def test_log_search():
    db = SessionLocal()
    initial_count = db.query(SearchHistory).count()
    log_search(db, "The Hobbit", "Resultado de exemplo")
    final_count = db.query(SearchHistory).count()
    assert final_count == initial_count + 1
    db.close()

def test_get_search_history():
    db = SessionLocal()
    log_search(db, "The Hobbit", "Resultado de exemplo")
    history = get_search_history(db)
    assert len(history) > 0
    assert history[0].query == "The Hobbit"
    db.close()
