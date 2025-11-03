from . import Base
from sqlalchemy import Column, Integer, DECIMAL, TIMESTAMP, ForeignKey, CheckConstraint, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

class Portfolio(Base):
    __tablename__ = "portfolios"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    artist_id = Column(UUID(as_uuid=True), ForeignKey('artists.id'), nullable=False)
    shares_amount = Column(Integer, default=0, nullable=False)
    average_buy_price = Column(DECIMAL(10, 2), default=0.00)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    __table_args__ = (
        UniqueConstraint('user_id', 'artist_id', name='uq_user_artist'),
        CheckConstraint('shares_amount >= 0', name='chk_shares_non_negative'),
        CheckConstraint('average_buy_price >= 0', name='chk_avg_price_non_negative'),
    )