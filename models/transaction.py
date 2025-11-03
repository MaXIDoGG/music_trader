from . import Base
from sqlalchemy import Column, String, Integer, DECIMAL, TIMESTAMP, ForeignKey, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    artist_id = Column(UUID(as_uuid=True), ForeignKey('artists.id'), nullable=False)
    type = Column(String(10), nullable=False)
    shares_amount = Column(Integer, nullable=False)
    price_per_share = Column(DECIMAL(10, 2), nullable=False)
    total_amount = Column(DECIMAL(15, 2), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    __table_args__ = (
        CheckConstraint("type IN ('buy', 'sell')", name='chk_transaction_type'),
        CheckConstraint('shares_amount > 0', name='chk_shares_amount_positive'),
        CheckConstraint('price_per_share > 0', name='chk_price_positive'),
        CheckConstraint('total_amount > 0', name='chk_total_amount_positive'),
    )