from pydantic import BaseModel, ConfigDict
from datetime import datetime

class TelegramMessageBase(BaseModel):
    """Base schema for Telegram messages"""
    source: str
    message: str
    sender_id: int
    timestamp: datetime
    status_description: str

class TelegramMessageCreate(TelegramMessageBase):
    """Schema for creating a new message"""
    pass

class TelegramMessage(TelegramMessageBase):
    """Schema for reading a message"""
    id: int

    model_config = ConfigDict(from_attributes=True)

