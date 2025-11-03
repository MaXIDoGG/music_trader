from . import Base
from sqlalchemy import Column, String, Integer, DECIMAL, TIMESTAMP, Text, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

class Artist(Base):
    __tablename__ = "artists"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    spotify_id = Column(String(100), unique=True, nullable=True)
    description = Column(Text)
    genre = Column(String(100))
    popularity_score = Column(Integer, default=0)
    total_shares = Column(Integer, default=1000000)
    available_shares = Column(Integer, default=1000000)
    current_price = Column(DECIMAL(10, 2), default=1.00)
    volatility = Column(DECIMAL(5, 4), default=0.0500)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    __table_args__ = (
        CheckConstraint('popularity_score >= 0 AND popularity_score <= 100', name='chk_popularity_range'),
        CheckConstraint('available_shares <= total_shares AND available_shares >= 0', name='chk_available_shares'),
    )