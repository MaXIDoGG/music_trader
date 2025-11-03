from . import BaseSchema
from typing import Optional
from pydantic import EmailStr
from datetime import datetime
import uuid

# Базовые схемы
class UserBase(BaseSchema):
    username: str
    email: EmailStr

# Создание пользователя (без ID и временных меток)
class UserCreate(UserBase):
    password: str

# Обновление пользователя (все поля опциональны)
class UserUpdate(BaseSchema):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    virtual_balance: Optional[float] = None

# Ответ API (включая ID и временные метки)
class UserResponse(UserBase):
    id: uuid.UUID
    virtual_balance: float
    created_at: datetime
    updated_at: datetime

# Ответ с токеном (для аутентификации)
class UserWithToken(UserResponse):
    access_token: str
    token_type: str = "bearer"

# Вход в систему
class UserLogin(BaseSchema):
    username: str
    password: str