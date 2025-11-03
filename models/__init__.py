from sqlalchemy import create_engine, Column, String, Integer, DECIMAL, TIMESTAMP, Text, UUID, ForeignKey, CheckConstraint, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
import uuid

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())