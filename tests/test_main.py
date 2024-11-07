import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..main import app, get_db
from ..db import Base
from ..services import get_movies

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture
def mock_get_movies(monkeypatch):
    def mock_get_movies():
        return {"docs": [{"name": "The Hobbit"}, {"name": "The Lord of the Rings"}]}
    monkeypatch.setattr("services.get_movies", mock_get_movies)

def test_search_movies(mock_get_movies):
    response = client.get("/movies")
    assert response.status_code == 200
    assert response.json() == [{"name": "The Hobbit"}, {"name": "The Lord of the Rings"}]

def test_search_movies_with_title(mock_get_movies):
    response = client.get("/movies?title=The Hobbit")
    assert response.status_code == 200
    assert response.json() == [{"name": "The Hobbit"}]

def test_search_history():
    response = client.get("/history")
    assert response.status_code == 200
    assert response.json() == []
    
    client.get("/movies?title=The Hobbit")
    
    response = client.get("/history")
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]["query"] == "The Hobbit"
