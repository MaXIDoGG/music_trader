from . import BaseSchema
from typing import Optional
from datetime import datetime
from enum import Enum
import uuid

class TransactionType(str, Enum):
    BUY = "buy"
    SELL = "sell"

class TransactionBase(BaseSchema):
    artist_id: uuid.UUID
    shares_amount: int
    type: TransactionType

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: uuid.UUID
    user_id: uuid.UUID
    price_per_share: float
    total_amount: float
    created_at: datetime

class TransactionWithDetails(TransactionResponse):
    artist_name: str
    username: str