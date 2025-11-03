from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import List

# Импорт моделей и схем
from models import Base
from schemas.user import UserCreate, UserResponse, UserLogin
from schemas.artist import ArtistCreate, ArtistResponse
from schemas.transaction import TransactionCreate, TransactionResponse
from schemas.portfolio import PortfolioResponse, UserPortfolioSummary

# Настройка базы данных
DATABASE_URL = "postgresql://postgres:postgres@localhost/music_trader"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создание таблиц
Base.metadata.create_all(bind=engine)

app = FastAPI(title="SoundStocks API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Зависимость для получения сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Заглушки для эндпоинтов (реализацию нужно добавить)
@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # TODO: Реализовать создание пользователя
    pass

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: str, db: Session = Depends(get_db)):
    # TODO: Реализовать получение пользователя
    pass

@app.post("/artists/", response_model=ArtistResponse)
def create_artist(artist: ArtistCreate, db: Session = Depends(get_db)):
    # TODO: Реализовать создание артиста
    pass

@app.get("/artists/", response_model=List[ArtistResponse])
def get_artists(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # TODO: Реализовать получение списка артистов
    pass

@app.post("/transactions/buy", response_model=TransactionResponse)
def buy_shares(transaction: TransactionCreate, db: Session = Depends(get_db)):
    # TODO: Реализовать покупку акций
    pass

@app.post("/transactions/sell", response_model=TransactionResponse)
def sell_shares(transaction: TransactionCreate, db: Session = Depends(get_db)):
    # TODO: Реализовать продажу акций
    pass

@app.get("/users/{user_id}/portfolio", response_model=UserPortfolioSummary)
def get_user_portfolio(user_id: str, db: Session = Depends(get_db)):
    # TODO: Реализовать получение портфеля пользователя
    pass