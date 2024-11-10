from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

DATABASE_URL = "sqlite:///./history.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class SearchHistory(Base):
    __tablename__ = "search_history"
    
    id = Column(Integer, primary_key=True, index=True)
    user = Column(String, nullable=False)  # Campo para armazenar o usuário
    query = Column(String, nullable=True)
    response = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(bind=engine)
