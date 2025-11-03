from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import uuid

class BaseSchema(BaseModel):
    class Config:
        from_attributes = True
        json_encoders = {
            uuid.UUID: str
        }