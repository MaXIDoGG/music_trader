from . import BaseSchema
from datetime import datetime
import uuid

class PortfolioBase(BaseSchema):
    user_id: uuid.UUID
    artist_id: uuid.UUID
    shares_amount: int
    average_buy_price: float

class PortfolioResponse(PortfolioBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

class PortfolioWithArtist(PortfolioResponse):
    artist_name: str
    artist_genre: str
    current_price: float
    total_value: float
    profit_loss: float

class UserPortfolioSummary(BaseSchema):
    total_investment: float
    current_value: float
    total_profit_loss: float
    portfolio_items: list[PortfolioWithArtist]