from . import BaseSchema
from typing import Optional
from datetime import datetime
import uuid

class ArtistBase(BaseSchema):
    name: str
    genre: Optional[str] = None
    description: Optional[str] = None

class ArtistCreate(ArtistBase):
    spotify_id: Optional[str] = None
    total_shares: int = 1000000
    current_price: float = 1.00
    volatility: float = 0.05

class ArtistUpdate(BaseSchema):
    name: Optional[str] = None
    genre: Optional[str] = None
    description: Optional[str] = None
    popularity_score: Optional[int] = None
    current_price: Optional[float] = None
    volatility: Optional[float] = None

class ArtistResponse(ArtistBase):
    id: uuid.UUID
    spotify_id: Optional[str]
    popularity_score: int
    total_shares: int
    available_shares: int
    current_price: float
    volatility: float
    created_at: datetime
    updated_at: datetime

class ArtistWithStats(ArtistResponse):
    total_investors: int
    total_volume: float
    price_change_24h: Optional[float] = None